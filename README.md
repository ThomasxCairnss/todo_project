
# Django To‑Do List Application

## Project Overview

This Django-based application is a to‑do list manager that lets users create, view, update, and delete tasks. It features an interactive dashboard with a summary of tasks (including a pie chart for completed vs. pending tasks) and a calendar view to track task due dates.

## Live Website:
https://todo-project-uakq.onrender.com/

## Installation and Local Setup

### Prerequisites
- Python 3.9 or later
- Git
- *(Optional)* Docker & docker-compose for a containerized setup

### Running Without Docker

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/todo_project.git
   cd todo_project
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv env
   ```
   - **On Windows:**
     ```bash
     env\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source env/bin/activate
     ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running With Docker

1. **Build and Start the Containers:**
   ```bash
   docker-compose up --build
   ```
   This command builds the Docker image and starts both the Django application and the PostgreSQL database.

2. **Access the Application:**  
   Open your browser and navigate to [http://localhost:8000](http://localhost:8000).

## Assumptions and Design Decisions

- **Assumptions:**
  - The project is built with Django 4.2 and Python 3.9+.
  - PostgreSQL is the preferred database, configured using `dj-database-url`.
  - Users require a straightforward, visually interactive interface for managing tasks.

- **Design Decisions:**
  - **Containerization:** Docker and docker-compose are used to ensure a consistent environment for both development and production.
  - **Modular Architecture:** The application is organized into separate modules for task management, calendar integration, and dashboard visualizations, improving maintainability.
  - **Enhanced User Experience:** Integration of Chart.js and FullCalendar provides interactive visualizations and an intuitive UI.
  - **Easy Deployment:** The project is structured to facilitate quick deployment with clear configurations for production environments.

