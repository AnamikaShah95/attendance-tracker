# 📋 Live Attendance Tracker

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)


A lightweight desktop application built with Python and Tkinter that tracks real-time attendance, prevents duplicate entries, logs exact check-in timestamps dynamically, and exports data instantly to an Excel-friendly CSV spreadsheet.

---

## 📂 Project Structure

```text
attendance-tracker/
├── app.py              # Main desktop application UI & logic
├── requirements.txt    # Project dependencies statement
└── README.md           # Project documentation


## ✨ Features

| Feature | Description |
| :--- | :--- |
| 🖥️ **Desktop GUI** | Clean, user-friendly graphical interface with a soft modern pastel design. |
| ⏱️ **Live Clock & Timestamps** | Includes a live, running digital clock and records exact check-in times. |
| 🛑 **Inline Validation** | Instantly alerts you to blank spaces or duplicate names without interrupting your workflow. |
| 📊 **Dynamic Counter** | Automatically scales and updates a real-time count of total attendees present. |
| 💾 **Excel Ready** | Automatically sorts names alphabetically and saves everything to a `daily_attendance.csv` file on close. |

---

## 🛠️ Quick Installation

```bash
# 1. Clone the repository
git clone [https://github.com/YOUR_USERNAME/attendance-tracker.git](https://github.com/YOUR_USERNAME/attendance-tracker.git)

# 2. Enter the workspace directory
cd attendance-tracker

# 3. Launch the desktop tracker app
python app.py
