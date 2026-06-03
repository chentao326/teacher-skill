"""
teacher-skill 学习状态持久化管理 (v2.1)

支持三个操作：
  --save <state.json>    保存当前学习状态（从 stdin 读取 JSON）
  --load <state.json>    读取学习状态并输出摘要
  --update <state.json> <json_patch>  更新指定字段
  --new <name>           创建新的学习会话（初始化状态）

状态文件存储在 teachers/{name}/learning-state.json
"""

import argparse
import json
import os
import sys
from datetime import datetime

STATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "teachers")


def default_state(name="default"):
    now = datetime.now().isoformat()
    return {
        "meta": {
            "name": name,
            "created_at": now,
            "updated_at": now,
            "version": "2.1.0"
        },
        "user": {
            "level": None,
            "familiar_fields": [],
            "learning_goal": "",
            "time_expectation": ""
        },
        "route": {
            "subject": "",
            "material_type": "",
            "total_units": 0,
            "units": []
        },
        "progress": {
            "status": "new",
            "current_unit_index": 0,
            "completed_units": [],
            "overall_percent": 0
        },
        "verification": {
            "checkpoints": [],
            "final_result": None
        }
    }


def load_state(path):
    if not os.path.exists(path):
        e = json.dumps({"error": "file not found: " + path})
        print(e)
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(path, state):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    state["meta"]["updated_at"] = datetime.now().isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(json.dumps({"status": "saved", "path": path}))


def print_summary(state):
    meta = state["meta"]
    user = state["user"]
    progress = state["progress"]
    verification = state["verification"]

    completed = len(progress["completed_units"])
    total = state["route"]["total_units"]
    percent = progress["overall_percent"]

    lines = []

    def add(key, val):
        lines.append(key + ": " + str(val))

    add("学习会话", meta["name"])
    add("状态", progress["status"])
    add("学科", state["route"].get("subject") or "未设置")

    if user.get("level"):
        m = {"beginner": "弱基础", "intermediate": "中等基础", "advanced": "强基础"}
        add("能力等级", m.get(user["level"], user["level"]))

    if user.get("familiar_fields"):
        add("熟悉领域", ", ".join(user["familiar_fields"]))

    if total > 0:
        add("进度", str(completed) + "/" + str(total) + " 单元 (" + str(percent) + "%)")
        if completed > 0:
            lines.append("已完成单元:")
            for u in progress["completed_units"]:
                rm = {"pass": "P", "partial": "~", "fail": "X"}
                mark = rm.get(u.get("result"), "?")
                wrong = ""
                if u.get("wrong_answers"):
                    wrong = " [错题: " + ", ".join(u["wrong_answers"]) + "]"
                lines.append("  " + mark + " " + u["name"] + wrong)

    if verification.get("checkpoints"):
        add("验证检查点", str(len(verification["checkpoints"])) + " 次")
        for cp in verification["checkpoints"]:
            add("  Phase " + str(cp.get("phase", "?")), "得分 " + str(cp.get("score", "N/A")))

    if verification.get("final_result"):
        passed = verification["final_result"].get("passed", False)
        add("最终验证", "通过" if passed else "待改进")

    print("\n".join(lines))


def deep_merge(base, overlay):
    for k, v in overlay.items():
        if k in base and isinstance(base[k], dict) and isinstance(v, dict):
            deep_merge(base[k], v)
        else:
            base[k] = v


def main():
    parser = argparse.ArgumentParser(description="teacher-skill learning state manager")
    parser.add_argument("--save", metavar="PATH", help="save state from stdin")
    parser.add_argument("--load", metavar="PATH", help="load and print state summary")
    parser.add_argument("--new", metavar="NAME", help="create new learning session")
    parser.add_argument("--update", nargs=2, metavar=("PATH", "JSON"),
                        help="update state fields")

    args = parser.parse_args()

    if args.new:
        state = default_state(args.new)
        path = os.path.join(STATE_DIR, args.new, "learning-state.json")
        save_state(path, state)
        print_summary(state)

    elif args.save:
        try:
            state = json.loads(sys.stdin.read())
        except json.JSONDecodeError as e:
            print(json.dumps({"error": "JSON parse failed: " + str(e)}))
            sys.exit(1)
        save_state(args.save, state)

    elif args.load:
        state = load_state(args.load)
        if state:
            print_summary(state)

    elif args.update:
        path, json_patch = args.update
        state = load_state(path)
        if not state:
            sys.exit(1)
        try:
            patch = json.loads(json_patch)
        except json.JSONDecodeError as e:
            print(json.dumps({"error": "JSON parse failed: " + str(e)}))
            sys.exit(1)
        deep_merge(state, patch)
        save_state(path, state)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
