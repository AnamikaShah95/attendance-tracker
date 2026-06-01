import csv
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# --- PALETTE DESIGN (Modern Soft Pastel) ---
BG_COLOR = "#FAF6F0"       # Soft cream background
CARD_BG = "#FFFFFF"        # Pure white for containment boxes
TEXT_MAIN = "#4A4238"      # Deep warm gray for text
ACCENT_PASTEL = "#AED6F1"  # Soft sky blue accent
BUTTON_ADD = "#A2D9CE"     # Pastel mint green
BUTTON_CLOSE = "#F1948A"   # Pastel soft rose
LIST_BORDER = "#E5E0D8"    # Subtle separator borders

class ModernAttendanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Tracker")
        self.root.geometry("440x580")
        self.root.configure(bg=BG_COLOR)
        
        self.attendance = {}
        
        # Build layout components
        self.setup_ui()
        self.update_live_clock()

    def setup_ui(self):
        # 1. Header Frame
        header_frame = tk.Frame(self.root, bg=BG_COLOR)
        header_frame.pack(fill="x", padx=25, pady=(20, 10))
        
        title_label = tk.Label(
            header_frame, text="Attendance Log", 
            font=("Segoe UI", 18, "bold"), fg=TEXT_MAIN, bg=BG_COLOR
        )
        title_label.pack(side="left")
        
        # Dynamic Clock Display
        self.clock_label = tk.Label(
            header_frame, text="", 
            font=("Segoe UI", 11, "italic"), fg="#888076", bg=BG_COLOR
        )
        self.clock_label.pack(side="right", pady=(5, 0))

        # 2. Input Card (White Box Container)
        input_card = tk.Frame(self.root, bg=CARD_BG, bd=0, highlightbackground=LIST_BORDER, highlightthickness=1)
        input_card.pack(fill="x", padx=25, pady=10)
        input_card.config(padx=15, pady=15)

        input_label = tk.Label(
            input_card, text="Register Name", 
            font=("Segoe UI", 10, "bold"), fg=TEXT_MAIN, bg=CARD_BG
        )
        input_label.pack(anchor="w", pady=(0, 5))

        # Core Controls Row
        control_row = tk.Frame(input_card, bg=CARD_BG)
        control_row.pack(fill="x")

        self.name_entry = tk.Entry(
            control_row, font=("Segoe UI", 12), bg=BG_COLOR, 
            fg=TEXT_MAIN, bd=0, relief="flat", highlightthickness=1, 
            highlightbackground=LIST_BORDER, highlightcolor=ACCENT_PASTEL
        )
        self.name_entry.pack(side="left", fill="x", expand=True, ipady=4, padx=(0, 8))
        self.name_entry.bind("<Return>", self.add_name)
        self.name_entry.focus()

        add_btn = tk.Button(
            control_row, text="Add", font=("Segoe UI", 10, "bold"),
            bg=BUTTON_ADD, fg=TEXT_MAIN, activebackground="#8ED1C4",
            relief="flat", bd=0, cursor="hand2", padx=15
        )
        add_btn.pack(side="right", ipady=3)
        add_btn.config(command=self.add_name)

        # Dynamic Inline Status Feedback
        self.status_label = tk.Label(input_card, text="", font=("Segoe UI", 9), bg=CARD_BG)
        self.status_label.pack(anchor="w", pady=(5, 0))

        # 3. List Display Card
        list_card = tk.Frame(self.root, bg=CARD_BG, bd=0, highlightbackground=LIST_BORDER, highlightthickness=1)
        list_card.pack(fill="both", expand=True, padx=25, pady=10)
        list_card.config(padx=15, pady=15)

        # Dynamic Registry Counter Head
        self.count_label = tk.Label(
            list_card, text="0 Present Currently", 
            font=("Segoe UI", 11, "bold"), fg=TEXT_MAIN, bg=CARD_BG
        )
        self.count_label.pack(anchor="w", pady=(0, 8))

        # Scrollable Custom Listbox
        list_frame = tk.Frame(list_card, bg=CARD_BG)
        list_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        self.attendance_listbox = tk.Listbox(
            list_frame, font=("Segoe UI", 11), bg=CARD_BG, fg=TEXT_MAIN,
            bd=0, highlightthickness=0, yscrollcommand=scrollbar.set,
            selectbackground=ACCENT_PASTEL, selectforeground=TEXT_MAIN, activestyle="none"
        )
        self.attendance_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.attendance_listbox.yview)

        # 4. Action Area (Bottom Button)
        save_btn = tk.Button(
            self.root, text="Save Records & Close Tracker", font=("Segoe UI", 11, "bold"),
            bg=BUTTON_CLOSE, fg="white", activebackground="#E57373",
            relief="flat", bd=0, cursor="hand2"
        )
        save_btn.pack(fill="x", padx=25, pady=(15, 25), ipady=6)
        save_btn.config(command=self.save_and_exit)

    # --- DYNAMIC FUNCTIONS ---
    def update_live_clock(self):
        """Updates the top right clock string dynamically every second."""
        now = datetime.now().strftime("%I:%M:%S %p")
        self.clock_label.config(text=now)
        self.root.after(1000, self.update_live_clock)

    def add_name(self, event=None):
        name = self.name_entry.get().strip().title()

        if not name:
            self.show_status("⚠️ Please input a valid name.", "#E74C3C")
            return

        if name in self.attendance:
            self.show_status(f"⚠️ {name} is already logged.", "#E67E22")
            self.name_entry.delete(0, tk.END)
            return

        # Record valid data row
        timestamp = datetime.now().strftime("%I:%M %p")
        self.attendance[name] = timestamp

        self.refresh_display()
        self.name_entry.delete(0, tk.END)
        self.show_status(f"✓ Registered {name} successfully.", "#27AE60")

    def show_status(self, text, color):
        self.status_label.config(text=text, fg=color)

    def refresh_display(self):
        self.attendance_listbox.delete(0, tk.END)
        
        # Alphabetical sorting
        for idx, k in enumerate(sorted(self.attendance.keys()), start=1):
            self.attendance_listbox.insert(tk.END, f"  {idx}. {k} — Registered at {self.attendance[k]}")
        
        # Dynamic Counter update
        self.count_label.config(text=f"📊 {len(self.attendance)} Present Currently")

    def save_and_exit(self):
        if not self.attendance:
            if messagebox.askyesno("Exit Tracker", "No logs present. Close application anyway?"):
                self.root.destroy()
            return

        filename = "daily_attendance.csv"
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Index No.", "Attendee Name", "Logged Time"])
                for idx, k in enumerate(sorted(self.attendance.keys()), start=1):
                    writer.writerow([idx, k, self.attendance[k]])
            
            messagebox.showinfo("Saved Successfully", f"Data safely exported directly to '{filename}'!")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Export Failure", f"Could not create storage file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernAttendanceApp(root)
    root.mainloop()
