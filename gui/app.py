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
            
            # Mark as done button (real button)
            if not done_today:
                btn = tk.Button(frame, text="Mark as Done", 
                            command=lambda n=name: self.mark_done(n))
                btn.pack(side="right")

    def mark_done(self, name):
        tracker.mark_done(name)
        messagebox.showinfo("Success", f"Habit '{name}' marked as done!")
        self.habits = tracker.get_all_habits()
        self.refresh_ui()


def run_gui():
    root = tk.Tk()
    app = MinutiaApp(root)
    root.mainloop()
