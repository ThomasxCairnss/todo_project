# Django To‑Do List Application

This is a Django-based To‑Do List application that allows users to create, view, update, and delete tasks. The app includes features such as task categorization, priority settings, a dashboard with pivot tables, and a calendar view integrated with FullCalendar. Additionally, it uses Docker for containerization and is configured for deployment using PostgreSQL with Render and Cloudflare for DNS management.

## Features

- **Task Management:**  
  Create, view, update, and delete tasks with fields such as title, description, due date, status (e.g., Pending, Completed), category, and priority.

- **Filtering and Sorting:**  
  Users can sort tasks (e.g., by due date) and filter tasks by status and priority.

- **Dashboard:**  
  Displays a summary of tasks along with a pie chart (using Chart.js) showing completed vs. pending tasks.

- **Calendar View:**  
  A full-page calendar (using FullCalendar) displays tasks on their due dates, with events colored based on task priority.

- **Containerization with Docker:**  
  The project is fully containerized using Docker and docker-compose.

- **Database:**  
  Uses PostgreSQL for production and is configured via `dj-database-url` for flexible deployment (with a default for local Docker setup).

- **Extra Credit (Optional):**  
  Includes creative functionality such as a calendar view and interactive dashboard elements.

## Technologies Used

- Python (3.9+)
- Django (4.2)
- PostgreSQL
- Docker & docker-compose
- Chart.js (for pie charts)
- FullCalendar (for calendar view)
- dj-database-url (for flexible database configuration)

## Local Setup

### Prerequisites

- Python 3.9 or later
- Docker & docker-compose
- Git

### Steps to Run Locally

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/todo_project.git
   cd todo_project
