from datetime import date
from habits import storage

def add_habit(name):
    habits = storage.load_data()
    for h in habits:
        if h["name"] == name:
            print(f"Habit '{name}' already exists.")
            return
    habits.append({
        "name": name,
        "created": str(date.today()),
        "log": []
    })
    storage.save_data(habits)
    print(f"Added habit: {name}")
