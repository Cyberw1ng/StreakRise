# StreakRise

StreakRise is a Python-based desktop GUI application built with Tkinter that helps you manage and track your daily routines and habits. It allows you to add routines, mark them as complete, and maintain streaks for consistency. The app also supports temporary routines that expire after a specified end date.

## Features

- **Add Routine**: Add new routines with a specified time.
- **Track Streaks**: Maintain streaks for routines to stay consistent.
- **Temporary Routines**: Add temporary routines that expire on a set date.
- **Logging**: Activity logging for added and completed routines.

## About

StreakRise is designed to help users develop and maintain daily habits by providing a simple and intuitive interface for managing routines. The application aims to motivate users through the concept of streaks 🔥, encouraging them to complete their routines consistently. Temporary routines allow flexibility for short-term goals.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Cyberw1ng/StreakRise.git
    cd streakRise
    ```

2. **Install dependencies**:
    The application uses Python's standard library, so no additional dependencies are required. Ensure you have Python 3.x installed.

## Usage

1. **Run the application**:
    ```sh
    python streakrise.py
    ```

2. **Add a Routine**:
    - Click the "Add Routine" button.
    - Enter the routine name and time (in HH: MM format).
    - Specify if the routine is temporary and, if so, provide the end date (in YYYY-MM-DD format).

3. **Complete a Routine**:
    - Click the "Complete" button next to the routine once it is done.
    - The button will be disabled if the routine is already completed for the day or the current time is past the routine's time.

## Files

- **streakrise.py**: Main application file containing the Tkinter interface and logic.
- **routines.json**: Stores the routines data in JSON format.
- **activity_log.txt**: Logs the activities such as adding and completing routines
