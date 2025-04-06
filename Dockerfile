FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the project
COPY . .

# Expose port 8000
EXPOSE 8000

# Use Gunicorn to serve the app, binding to the port provided by Render, or default to 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn todo_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
