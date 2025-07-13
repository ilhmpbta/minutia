import sys
from habits import tracker

def print_help():
    print("Usage:")
    print("  python main.py add \"habit name\"")
    print("  python main.py done \"habit name\"")
    print("  python main.py history")
    print("  python main.py delete \"Habit name\"")
    print("  python main.py streak")
    print("  python main.py export")
    print("  python main.py check")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "add":
        if len(sys.argv) < 3:
            print("Please provide habit name.")
        else:
            tracker.add_habit(sys.argv[2])

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Please provide habit name.")
        else:
            tracker.mark_done(sys.argv[2])

    elif cmd == "history":
        tracker.show_history()

    elif cmd == "delete":
        if len(sys.argv) < 3:
            print("Please provide habit name.")
        else:
            tracker.delete_habit(sys.argv[2])

    elif cmd == "streak":
        if len(sys.argv) < 3:
            print("Please provide habit name.")
        else:
            tracker.check_streak(sys.argv[2])

    elif cmd == "export":
        tracker.export_csv()
        
    elif cmd == "check":
        tracker.check_pending_today()

    elif cmd == "gui":
        from gui.app import run_gui
        run_gui()

    else:
        print(f"Unknown command: {cmd}")
        print_help()
