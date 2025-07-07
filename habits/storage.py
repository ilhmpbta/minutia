import json
import os

DATA_FILE = "./data/habits.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(habits):
    with open(DATA_FILE, "w") as f:
        json.dump(habits, f, indent=2)
