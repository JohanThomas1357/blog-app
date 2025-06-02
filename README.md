# blog-app

Overview

This is a full-stack blog application that allows users to create, read, update, and delete blog posts. It features a RESTful API backend and a modern React-based frontend, providing a seamless experience for managing and sharing blog content.

Features

User Authentication: Register and log in to manage blog posts.
Create Blog Posts: Write and publish blog posts via an intuitive interface.
Edit/Delete Posts: Modify or remove your existing posts.
View Blogs: Browse posts on the homepage.
Responsive Design: Optimized for both desktop and mobile devices using Tailwind CSS.

Tech Stack
Frontend: React.js, Tailwind CSS
Backend: Python (Django with Django REST Framework)
Database: SQLite (default for Django, can be configured for other databases like PostgreSQL)
Other Tools: Axios (assumed for API requests in React), React Router (assumed for navigation)

Prerequisites
To run this project locally, ensure you have the following installed:
Python (v3.8 or higher)
Node.js (v16.x or higher)
npm (v8.x or higher)
Git

Installation

Clone the Repository:
git clone https://github.com/JohanThomas1357/blog-app.git
cd blog-app

Set Up the Backend:
Navigate to the backend directory:
cd backend
Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r backend_requirements.txt
Run migrations to set up the database:
python manage.py makemigrations
python manage.py migrate

Start the backend server:
python manage.py runserver
The backend API should be accessible at http://localhost:8000.

Set Up the Frontend:
Navigate to the frontend directory:

cd frontend

Install dependencies:

npm install

Start the frontend development server:

npm start

The frontend should be accessible at http://localhost:3000.

Usage

Register/Login: Create an account or log in to access full functionality.

Create a Post: Navigate to the "Create Post" section, write your content, and publish.

Manage Posts: Edit or delete your posts from your dashboard.

Explore: Browse other users' posts on the homepage.


Project Structure

backend/: Contains the Django backend.

user/: Django app for user management and blog functionality.

manage.py: Django management script.

backend_requirements.txt: Backend dependencies.

frontend/: Contains the React frontend.

src/: React components, styles, and logic.

public/: Static assets like index.html.

tailwind.config.js: Tailwind CSS configuration.

package.json: Frontend dependencies.
