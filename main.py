import sys

def print_help():
    print("Usage:")
    print("  python main.py add \"habit name\"")
    print("  python main.py done \"habit name\"")
    print("  python main.py history")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
    else:
        print(f"Command: {sys.argv[1]}")
