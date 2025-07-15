from datetime import date
from habits import storage
from datetime import datetime, timedelta
import csv

def add_habit(name):
    habits = storage.load_data()
    for h in habits:
        if h["name"].lower() == name.lower():
            print(f"Habit '{name}' already exists.")
            return
    habits.append({
        "name": name,
        "created": str(date.today()),
        "log": []
    })
    storage.save_data(habits)
    print(f"Added habit: {name}")

def mark_done(name):
    habits = storage.load_data()
    today = str(date.today())
    found = False

    for habit in habits:
        if habit["name"].lower() == name.lower():
            found = True
            if today not in habit["log"]:
                habit["log"].append(today)
                print(f"Habit '{name}' marked as done for today.")
            else:
                print(f"Habit '{name}' is already marked done today.")
            break

    if not found:
        print(f"Habit '{name}' not found.")

    storage.save_data(habits)

def show_history():
    habits = storage.load_data()
    if not habits:
        print("No habits found.")
        return

    for habit in habits:
        print(f"\n📝 {habit['name']}")
        print(f"  Created: {habit['created']}")
        print(f"  Days Done: {len(habit['log'])}")
        if habit['log']:
            print(f"  Log: {', '.join(habit['log'])}")

def delete_habit(name):
    habits = storage.load_data()
    new_habits = [h for h in habits if h["name"].lower() != name.lower()]

    if len(new_habits) == len(habits):
        print(f"Habit '{name}' not found.")
    else:
        storage.save_data(new_habits)
        print(f"Habit '{name}' deleted.")

def check_streak(name):
    habits = storage.load_data()
    for h in habits:
        if h["name"].lower() == name.lower():
            if not h["log"]:
                print(f"No history found for '{name}'.")
                return

            sorted_log = sorted(h["log"], reverse=True)
            streak = 0
            today = datetime.today().date()

            for i, date_str in enumerate(sorted_log):
                date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
                expected = today - timedelta(days=streak)
                if date_obj == expected:
                    streak += 1
                else:
                    break

            print(f"Streak for '{name}': {streak} day(s)")
            print(f"Last done: {sorted_log[0]}")
            return

    print(f"Habit '{name}' not found.")

def export_to_csv(filename="habits_export.csv"):
    habits = storage.load_data()
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Habit Name", "Created", "Log Dates"])
        for h in habits:
            writer.writerow([h["name"], h["created"], "; ".join(h["log"])])
    print("Data exported to export.csv")

def check_pending_today():
    habits = storage.load_data()
    today = str(date.today())

    if not habits:
        print("No habits found.")
        return

    print(f"Habit status for today ({today}):\n")
    for habit in habits:
        status = "✅ Done" if today in habit["log"] else "⚠️ Not done"
        print(f"- {habit['name']}: {status}")

def get_all_habits():
    return storage.load_data()

def is_done_today(name):
    today = str(date.today())
    habits = storage.load_data()
    for h in habits:
        if h["name"].lower() == name.lower():
            return today in h["log"]
    return False

def delete_habit(name):
    habits = storage.load_data()
    habits = [h for h in habits if h["name"].lower() != name.lower()]
    storage.save_data(habits)

from datetime import datetime, timedelta

def get_streak(name):
    habits = storage.load_data()
    for h in habits:
        if h["name"].lower() == name.lower():
            log = sorted([datetime.fromisoformat(d) for d in h["log"]], reverse=True)
            if not log:
                return 0

            streak = 1
            today = datetime.today().date()

            # Kalau hari ini belum ditandai done, streak dihitung dari kemarin
            if today != log[0].date():
                expected = today - timedelta(days=1)
            else:
                expected = today

            for date_done in log:
                if date_done.date() == expected:
                    streak += 1
                    expected -= timedelta(days=1)
                else:
                    break
            return streak
    return 0
