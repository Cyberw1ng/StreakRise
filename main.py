import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk
from datetime import datetime, date
import json
import os

# Constants
ROUTINES_FILE = "routines.json"
LOG_FILE = "activity_log.txt"

# Load routines
def load_routines():
    if os.path.exists(ROUTINES_FILE):
        try:
            with open(ROUTINES_FILE, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            return {}
    return {}

# Save routines
def save_routines(routines):
    with open(ROUTINES_FILE, "w") as file:
        json.dump(routines, file)

# Log activity
def log_activity(activity):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()}: {activity}\n")

# Main application class
class StrakRiseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Strak Rise")

        # Set the theme
        self.style = ttk.Style()
        self.style.theme_use('clam')  # Using 'clam' for a modern look

        # Configure styles
        self.style.configure('TButton', font=('Helvetica', 10), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 12))
        self.style.configure('TFrame', background='#f0f0f0')

        self.routines = load_routines()
        self.create_widgets()
        self.update_routines_display()

    def create_widgets(self):
        self.add_routine_button = ttk.Button(self.root, text="Add Routine", command=self.add_routine)
        self.add_routine_button.pack(pady=10)

        self.routines_frame = ttk.Frame(self.root, padding="10")
        self.routines_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def add_routine(self):
        routine_name = simpledialog.askstring("Routine", "Enter the routine:")
        routine_time_str = simpledialog.askstring("Time", "Enter the time (HH:MM):")
        try:
            routine_time = datetime.strptime(routine_time_str, "%H:%M").time()
        except ValueError:
            messagebox.showerror("Invalid time", "Please enter a valid time in HH:MM format.")
            return

        is_temporary = messagebox.askyesno("Routine Type", "Is this a temporary routine?")
        end_date_str = None
        if is_temporary:
            end_date_str = simpledialog.askstring("End Date", "Enter the end date (YYYY-MM-DD):")
            try:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
                if end_date < date.today():
                    messagebox.showerror("Invalid date", "End date must be in the future.")
                    return
            except ValueError:
                messagebox.showerror("Invalid date", "Please enter a valid date in YYYY-MM-DD format.")
                return

        self.routines[routine_name] = {
            "time": routine_time_str,
            "streak": 0,
            "last_completed": None,
            "temporary": is_temporary,
            "end_date": end_date_str
        }
        save_routines(self.routines)
        log_activity(f"Added routine: {routine_name} at {routine_time_str}, Temporary: {is_temporary}, End Date: {end_date_str}")
        self.update_routines_display()

    def update_routines_display(self):
        for widget in self.routines_frame.winfo_children():
            widget.destroy()

        for routine, details in self.routines.items():
            if details['temporary'] and details['end_date']:
                end_date = datetime.strptime(details['end_date'], "%Y-%m-%d").date()
                if date.today() > end_date:
                    del self.routines[routine]
                    continue

            frame = ttk.Frame(self.routines_frame)
            frame.pack(fill=tk.X, pady=5)

            routine_label = ttk.Label(frame, text=f"{routine} - Report Time: {details['time']}", style='White.TLabel')
            routine_label.pack(side=tk.LEFT, padx=5)

            streak_label = ttk.Label(frame, text=f"🔥 Streak: {details['streak']}", style='White.TLabel')
            streak_label.pack(side=tk.LEFT, padx=5)

            now = datetime.now().time()
            routine_time = datetime.strptime(details['time'], "%H:%M").time()
            if details['last_completed'] == datetime.now().date().isoformat() or now > routine_time:
                complete_button = ttk.Button(frame, text="Complete", state=tk.DISABLED)
            else:
                complete_button = ttk.Button(frame, text="Complete", command=lambda r=routine: self.complete_routine(r))
            complete_button.pack(side=tk.RIGHT, padx=5)

        save_routines(self.routines)

    def complete_routine(self, routine):
        now = datetime.now()
        self.routines[routine]['last_completed'] = now.date().isoformat()
        self.routines[routine]['streak'] += 1
        save_routines(self.routines)
        log_activity(f"Completed routine: {routine}")
        self.update_routines_display()

if __name__ == "__main__":
    root = tk.Tk()
    app = StrakRiseApp(root)
    root.mainloop()
