import sys
from habits import tracker

def print_help():
    print("Usage:")
    print("  python main.py add \"habit name\"")
    print("  python main.py done \"habit name\"")
    print("  python main.py history")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("Please provide a habit name.")
        else:
            habit_name = sys.argv[2]
            tracker.add_habit(habit_name)

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Please provide habit name.")
        else:
            tracker.mark_done(sys.argv[2])

    elif cmd == "history":
        print("Coming soon: view habit history!")

    else:
        print(f"Unknown command: {cmd}")
        print_help()
