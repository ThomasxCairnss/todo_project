FROM python:3.9-slim

# Prevent Python from writing .pyc files and enable unbuffered output
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --upgrade pip --root-user-action=ignore && pip install -r requirements.txt --root-user-action=ignore

# Copy the rest of the project files
COPY . .

# Expose port 8000 (Render will set $PORT at runtime)
EXPOSE 8000

# Run migrations and start the server with Gunicorn, binding to $PORT or defaulting to 8000
CMD ["sh", "-c", "python manage.py migrate && gunicorn todo_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}"]
