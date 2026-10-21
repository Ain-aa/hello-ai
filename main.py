import argparse
import sys
from datetime import datetime


def build_greeting(name: str, repeat: int = 1) -> str: 
    """根据名字生成带时间戳的问候语。"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] 你好，{name}！欢迎开始 AI 学习之旅。"
    return "\n".join(line for _ in range(repeat))


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="我的第一个 Python 项目")
    parser.add_argument("--name", default="同学", help="要问候的人")
    parser.add_argument("--repeat", type=int, default=1, help="重复次数")
    parser.add_argument("--upper", action="store_true", help="输出转为大写")
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
  
    result = build_greeting(args.name, args.repeat)
    if args.upper:
        result = result.upper()
    print(result)

if __name__ == "__main__":
    raise SystemExit(main())