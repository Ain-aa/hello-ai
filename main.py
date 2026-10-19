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
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    if args.repeat < 1:
        print("错误：--repeat 必须大于 0", file=sys.stderr)
        return 1
    print(build_greeting(args.name, args.repeat))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())