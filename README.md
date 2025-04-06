Django To‑Do List Application

This is a Django-based web application for managing a To‑Do List. Users can create, view, update, and delete tasks with fields such as title, description, due date, status, category, and priority. The application includes a dashboard with a task summary, a calendar view (using FullCalendar), and a pie chart (via Chart.js) that shows the proportion of completed versus pending tasks.

Live URL: https://todo-project-uakq.onrender.com/

Features:

Task Management: Create, read, update, and delete tasks.

Filtering & Sorting: Users can sort tasks (by due date, status, or priority) and filter them by status and priority.

Dashboard: Displays total, completed, and pending tasks along with a pie chart for task completion.

Calendar View: Uses FullCalendar to display tasks on a calendar based on their due dates.

Dockerized Application: Fully containerized using Docker and docker-compose.

PostgreSQL Database: Configured via dj-database-url for production, with a default for local Docker setup.

Deployment Ready: Includes instructions for deployment using free services (Render, Fly.io, or PythonAnywhere) and Cloudflare DNS management for custom domains.

Technologies Used:

Python 3.9+

Django 4.2

PostgreSQL

Docker & docker-compose

Chart.js

FullCalendar

dj-database-url

Local Setup

Prerequisites:

Python 3.9 or later

Docker & docker-compose (if using containerized development)

Git

Running Without Docker:

Clone the Repository: git clone https://github.com/your-username/todo_project.git cd todo_project

Create and Activate a Virtual Environment: python -m venv env On Windows: env\Scripts\activate On macOS/Linux: source env/bin/activate

Install Dependencies: pip install -r requirements.txt

Apply Migrations: python manage.py makemigrations python manage.py migrate

Run the Development Server: python manage.py runserver 0.0.0.0:8000 Then open your browser and navigate to http://localhost:8000

Running With Docker:

Build and Start the Containers: docker-compose up --build This builds the Docker image and starts two services:

web: Runs the Django app.

db: Runs the PostgreSQL database.

Access the Application: Visit http://localhost:8000 in your browser.

Docker Configuration

Dockerfile (located at the project root):
FROM python:3.9-slim

Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1 ENV PYTHONUNBUFFERED 1

Set the working directory
WORKDIR /app

Copy requirements and install them
COPY requirements.txt . RUN pip install --upgrade pip && pip install -r requirements.txt

Copy the rest of the project files
COPY . .

Expose port 8000 (Render will pass $PORT during deployment)
EXPOSE 8000

Run migrations and start the server with Gunicorn, binding to $PORT or defaulting to 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn todo_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]

docker-compose.yml (located at the project root):
version: '3' services: web: build: . ports: - "8000:8000" volumes: - .:/app depends_on: - db db: image: postgres:13 environment: POSTGRES_DB: todo_db POSTGRES_USER: todo_user POSTGRES_PASSWORD: your_password ports: - "5432:5432" volumes: - postgres_data:/var/lib/postgresql/data

volumes: postgres_data:

Database Configuration

In todo_project/settings.py, the database is configured using dj-database-url: DATABASES = { 'default': dj_database_url.config( default=os.environ.get('DATABASE_URL', 'postgres://todo_user:your_password@db:5432/todo_db') ) } Locally, the default uses host "db" as defined in docker-compose.yml. In production, set DATABASE_URL to your external PostgreSQL connection string.

Deployment on Render

Provision a PostgreSQL Database on Render:

Log in to Render and create a new PostgreSQL database.

Render will provide both an internal and an external connection string.

Use the external connection string, for example: postgresql://todo_db_dz7h_user:TtfeGvUg1NlRaYxtS3TCRRQQFLWdKeUO@dpg-cvp60mq4d50c73boov00-a.oregon-postgres.render.com/todo_db_dz7h

Configure Your Django Web Service on Render:

Connect your repository to Render.

In your Render web service settings, add the following environment variables: DATABASE_URL = (external connection string from above) SECRET_KEY = (your secret key, e.g., 11807155004e412e2fda1d024036cdb5) DEBUG = False ALLOWED_HOSTS = todo-project-uakq.onrender.com

Render will build your Docker image (using your Dockerfile) and deploy your service.

Live Deployment: Once deployed, your application will be accessible at: Render URL: https://todo-project-uakq.onrender.com Custom Domain: (if configured via Cloudflare)

Environment Variables (Production):

SECRET_KEY: A long, random secret key.

DATABASE_URL: The full external PostgreSQL connection string.

DEBUG: False

ALLOWED_HOSTS: Include your Render domain (e.g., todo-project-uakq.onrender.com)

Extra Features:

Calendar View: Uses FullCalendar to display tasks by due dates.

Dashboard with Pie Chart: Uses Chart.js to display a pie chart of completed vs. pending tasks.

Filtering & Sorting: Users can sort and filter tasks using query parameters.

Contribution: Feel free to fork the repository and submit pull requests. For suggestions or feature requests, please open an issue.

License: This project is licensed under the MIT License.

Live Deployment:

Render URL: https://todo-project-uakq.onrender.com

Custom Domain: (if configured)

Troubleshooting:

Docker Build Issues: If you encounter errors during the Docker build, try: docker builder prune --all docker system prune --all Then rebuild with: docker-compose up --build

Database Connection Issues: Verify that DATABASE_URL is set correctly in your Render environment.

Port Binding Issues: Ensure your Dockerfile binds to 0.0.0.0:${PORT:-8000} using Gunicorn.

Asset Loading: If external assets (e.g., FullCalendar, Chart.js) fail to load, check your browser's network tab.

Filtering & Sorting: Verify that query parameters are passed correctly and that your view logic handles them as expected.
