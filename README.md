-E-Learning Platform
This project is an e-learning platform built with Django 5. The platform allows instructors to create courses with various modules, lessons, and quizzes, while students can enroll in courses, view content, and track their progress.

*Features:
    -Course Management: Instructors can create, update, and organize courses into different modules and lessons.
    -Student Enrollment: Students can enroll in courses and access course content.
    -Content Types: Supports text, video, image, and file content for versatile learning experiences.

*Technologies:
    -Python 3.11+
    -Django 5.1.2
    -Django REST Framework for API development
    -SQLite for development
    -Celery with Redis for background tasks
    -HTML/CSS for frontend interactions(django templates)


*Getting Started:
    Follow these steps to set up the project on your local environment.

        *Prerequisites:
        Python 3.11+
        PostgreSQL (for production) or SQLite (for development)
        Redis for task queue (if using Celery)


*Installation:
    1.Clone the repository:

        git clone https://github.com/seela-2001/e-learning-platform.git
        cd e-learning-platform

    2.pip install poetry 
      poetry shell

    3.pip install -r requirements.txt

    4.Apply migrations:
        python manage.py makemigrations
        pyton manage.py migrate

