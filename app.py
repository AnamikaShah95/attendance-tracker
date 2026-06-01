import csv
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Initialize the main dictionary to hold attendance data
attendance = {}


def add_name(event=None):
    """Adds the name from the input field to the attendance list."""
    name = name_entry.get().strip().title()

    if name == "":
        messagebox.showwarning("Input Error", "Please enter a name.")
        return

    if name in attendance:
        messagebox.showwarning("Duplicate", f"{name} is already marked present!")
        name_entry.delete(0, tk.END)
        return

    # Get current timestamp
    current_time = datetime.now().strftime("%H:%M:%S")
    attendance[name] = current_time

    # Refresh the visual listbox
    update_listbox()

    # Clear the entry field for the next name
    name_entry.delete(0, tk.END)
    status_label.config(text=f"✓ Added {name}", fg="green")


def update_listbox():
    """Sorts and updates the display listbox."""
    # Clear current listbox items
    attendance_listbox.delete(0, tk.END)

    # Insert sorted names
    for index, name in enumerate(sorted(attendance.keys()), start=1):
        attendance_listbox.insert(
            tk.END, f"{index}. {name} (Arrived: {attendance[name]})"
        )

    # Update total count label
    count_label.config(text=f"Total Present: {len(attendance)}")


def save_and_exit():
    """Saves data to CSV and closes the app."""
    if not attendance:
        if messagebox.askyesno(
            "Exit", "No attendance recorded. Are you sure you want to exit?"
        ):
            root.destroy()
        return

    filename = "daily_attendance.csv"

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["No.", "Name", "Check-in Time"])

            for index, name in enumerate(sorted(attendance.keys()), start=1):
                writer.writerow([index, name, attendance[name]])

        messagebox.showinfo(
            "Saved", f"Attendance successfully saved to '{filename}'!"
        )
        root.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Could not save file: {e}")


# --- GUI LAYOUT SETUP ---

# 1. Create main window
root = tk.Tk()
root.title("Attendance Tracker")
root.geometry("400x500")
root.configure(padx=20, pady=20)

# 2. Title Header
title_label = tk.Label(
    root, text="Attendance Log", font=("Arial", 16, "bold")
)
title_label.pack(pady=(0, 15))

# 3. Input Frame (Label + Entry Box + Button)
input_frame = tk.Frame(root)
input_frame.pack(fill="x", pady=5)

name_entry = ttk.Entry(input_frame, font=("Arial", 12))
name_entry.pack(side="left", fill="x", expand=True, padx=(0, 5))
# Allows pressing 'Enter' on keyboard to add name
name_entry.bind("<Return>", add_name)

add_button = ttk.Button(input_frame, text="Add", command=add_name)
add_button.pack(side="right")

# 4. Feedback Status Label
status_label = tk.Label(root, text="", font=("Arial", 10, "italic"))
status_label.pack(pady=5)

# 5. Listbox Display (With Scrollbar)
list_frame = tk.Frame(root)
list_frame.pack(fill="both", expand=True, pady=10)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

attendance_listbox = tk.Listbox(
    list_frame, font=("Arial", 11), yscrollcommand=scrollbar.set
)
attendance_listbox.pack(side="left", fill="both", expand=True)
scrollbar.config(command=attendance_listbox.yview)

# 6. Bottom Stats and Exit Button
count_label = tk.Label(
    root, text="Total Present: 0", font=("Arial", 11, "bold")
)
count_label.pack(anchor="w", pady=5)

save_button = tk.Button(
    root,
    text="Save & Close Application",
    bg="#d9534f",
    fg="white",
    font=("Arial", 11, "bold"),
    command=save_and_exit,
)
save_button.pack(fill="x", pady=(10, 0))

# Run the application loop
root.mainloop()