# Full-Stack Django Calculator Web Application

A full-stack calculator web application built with **Python, Django, HTML, CSS, and SQLite**. It connects a responsive frontend interface with Django's MVT/MVC backend logic to evaluate mathematical expressions and store calculation history in a database.

## Features
- **Interactive Calculator UI:** Clean, responsive button grid for arithmetic operations (`+`, `-`, `*`, `/`, decimals).
- **Database-Backed History:** Automatically saves every calculation expression and result to an SQLite database.
- **History Management:** Displays the latest calculations and allows clearing the history with a single click.
- **Input Validation:** Safely validates user expressions before evaluation to prevent errors.

## Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite
- **Version Control:** Git & GitHub

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Navigate to the project directory and run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```
4. Open `http://127.0.0` in your browser.
