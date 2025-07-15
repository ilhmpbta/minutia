import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
import tkinter as tk
from habits import tracker
from tkinter import messagebox

class MinutiaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minutia - Habit Tracker")
        self.root.geometry("400x400")
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)

        self.habits = tracker.get_all_habits()

        self.refresh_ui()

    def refresh_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title using Button styled as label (normal label wouldnt show, so I had to improvise)
        title = tk.Button(self.root, text="Your Habits Today", 
                        font=("Arial", 16), fg="white", bg="black",
                        state="disabled", relief="flat", bd=0)
        title.pack(pady=10)
        
        for habit in self.habits:
            frame = tk.Frame(self.root, bg="black")
            frame.pack(fill="x", padx=20, pady=5)
            
            name = habit["name"]
            done_today = tracker.is_done_today(name)
            
            # Habit name using Button styled as label (normal label wouldnt show)
            name_button = tk.Button(frame, text=name, width=20, anchor="w", 
                                fg="white", bg="black", font=("Arial", 12),
                                state="disabled", relief="flat", bd=0)
            name_button.pack(side="left")
            
            # Status using Button styled as label (normal label wouldnt show)
            status = "✅" if done_today else "❌"
            status_button = tk.Button(frame, text=status, fg="white", bg="black",
                                    font=("Arial", 12), state="disabled", 
                                    relief="flat", bd=0)
            status_button.pack(side="left")

            del_btn = tk.Button(frame, text="🗑", command=lambda n=name: self.delete_habit(n),
                    fg="red", bg="black", relief="flat", font=("Arial", 12))
            del_btn.pack(side="right")
            
            streak_count = tracker.get_streak(name)
            streak_label = tk.Button(frame, text=f"🔥 {streak_count}", fg="orange", bg="black",
                                    font=("Arial", 10), state="disabled", relief="flat", bd=0)
            streak_label.pack(side="left")

            # Mark as done button (real button)
            if not done_today:
                btn = tk.Button(frame, text="Mark as Done", 
                            command=lambda n=name: self.mark_done(n))
                btn.pack(side="right")

        # Button to add habits on the bottom side of the app
        add_btn = tk.Button(self.root, text="➕ Add Habit", command=self.add_habit_popup,
                fg="white", bg="black", relief="flat", font=("Arial", 12))
        add_btn.pack(pady=10)

        export_btn = tk.Button(self.root, text="📤 Export CSV", command=self.export_csv, 
                fg="white", bg="black", relief="flat", font=("Arial", 12))
        export_btn.pack(pady=5)

    def mark_done(self, name):
        tracker.mark_done(name)
        messagebox.showinfo("Success", f"Habit '{name}' marked as done!")
        self.habits = tracker.get_all_habits()
        self.refresh_ui()

    def add_habit_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Add New Habit")
        popup.geometry("250x100")
        popup.configure(bg="black")

        tk.Label(popup, text="Habit Name:", fg="white", bg="black").pack(pady=5)
        entry = tk.Entry(popup)
        entry.pack()

        def submit():
            name = entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Habit name cannot be empty.")
                return

            if any(h["name"].lower() == name.lower() for h in self.habits):
                messagebox.showwarning("Duplicate", f"Habit '{name}' already exists.")
                return

            tracker.add_habit(name)
            self.habits = tracker.get_all_habits()
            self.refresh_ui()
            popup.destroy()

        tk.Button(popup, text="Add", command=submit).pack(pady=5)

    def delete_habit(self, name):
        confirm = messagebox.askyesno("Confirm", f"Delete habit '{name}'?")
        if confirm:
            tracker.delete_habit(name)
            self.habits = tracker.get_all_habits()
            self.refresh_ui()

    def export_csv(self):
        tracker.export_to_csv()
        messagebox.showinfo("Exported", "Habits exported to habits_export.csv")

def run_gui():
    root = tk.Tk()
    app = MinutiaApp(root)
    root.mainloop()
