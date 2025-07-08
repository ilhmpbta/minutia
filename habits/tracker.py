from datetime import date
from habits import storage

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
