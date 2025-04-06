# Django To‑Do List Application

This is a Django-based web application for managing a To‑Do List. Users can create, view, update, and delete tasks with fields such as title, description, due date, status, category, and priority. The application includes a dashboard with a task summary, a calendar view for tasks using FullCalendar, and a pie chart (via Chart.js) that shows the proportion of completed vs. pending tasks.

## Features

- **Task Management:** Create, read, update, and delete tasks.
- **Filtering & Sorting:** Users can sort tasks (by due date, status, or priority) and filter them by status and priority.
- **Dashboard:** Displays total, completed, and pending tasks, along with a pie chart for task completion.
- **Calendar View:** Uses FullCalendar to display tasks on a calendar based on their due dates.
- **Dockerized Application:** Fully containerized using Docker and docker-compose.
- **PostgreSQL Database:** Configured via `dj-database-url` for production, with a default for local Docker setup.
- **Deployment Ready:** Instructions for deployment using free services (Render, Fly.io, or PythonAnywhere) and Cloudflare DNS management for custom domains.

## Technologies Used

- Python 3.9+
- Django 4.2
- PostgreSQL
- Docker & docker-compose
- Chart.js
- FullCalendar
- dj-database-url

## Local Setup

### Prerequisites

- Python 3.9 or later
- Docker & docker-compose (if using containerized development)
- Git

### Running Without Docker

1. **Clone the Repository:**

-git clone https://github.com/your-username/todo_project.git
-cd todo_project

2. **Create and Activate a Virtual Environment:**
-python -m venv env
# On Windows:
-env\Scripts\activate
# On macOS/Linux:
-source env/bin/activate
3. **Install Dependencies:**
- pip install -r requirements.txt
4. **Apply Migrations:**
-python manage.py makemigrations
-python manage.py migrate
5. **Running with Docker**
-docker-compose up --build

##This command builds the Docker image and starts the following services:
web: Runs the Django app.
db: Runs the PostgreSQL database.

6. **Access the Application:**
Visit http://localhost:8000 in your browser.
