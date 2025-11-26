# First Homework
Create a TODO application using Python with Django (https://github.com/DataTalksClub/ai-dev-tools-zoomcamp/blob/main/cohorts/2025/01-overview/homework.md)

 
<img width="876" height="971" alt="imagen" src="https://github.com/user-attachments/assets/47cc9ad2-ab90-48b4-913e-e4acb2993bd2" />

# Django TODO App

A simple TODO application built with Django as part of the AI-Assisted Development homework for the AI Dev Tools Zoomcamp.

## Features

- ✅ Create TODOs with title, description, and due date
- ✅ Edit existing TODOs
- ✅ Delete TODOs
- ✅ Mark TODOs as resolved/completed
- ✅ Beautiful gradient UI with smooth animations
- ✅ Fully tested with Django test suite

## Technologies Used

- Python
- Django
- HTML/CSS
- SQLite (database)

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

2. **Install Django**
```bash
pip install django
```

3. **Navigate to project directory**
```bash
cd todoproject
```

4. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Run tests (optional but recommended)**
```bash
python manage.py test
```

6. **Start the development server**
```bash
python manage.py runserver
```

7. **Open your browser and visit**
```
http://127.0.0.1:8000
```

## Commands Reference

| Command | Description |
|---------|-------------|
| `pip install django` | Downloads and installs Django framework |
| `python -m django startproject todoproject` | Creates a new Django project with all necessary files |
| `cd todoproject` | Changes directory to enter the project folder |
| `python manage.py startapp todoapp` | Creates a new app within the project |
| `mkdir templates` | Creates a folder to store HTML template files |
| `python manage.py makemigrations` | Detects changes in models and creates migration files |
| `python manage.py migrate` | Applies migrations and creates/updates database tables |
| `python manage.py test` | Runs all test cases to verify everything works |
| `python manage.py runserver` | Starts local development server at http://127.0.0.1:8000 |

## Project Structure
```
todoproject/
├── todoproject/          # Main project settings
│   ├── settings.py      # Project configuration
│   ├── urls.py          # Main URL routing
│   └── ...
├── todoapp/             # TODO application
│   ├── models.py        # Database models (Todo model)
│   ├── views.py         # Business logic and request handlers
│   ├── urls.py          # App-specific URL routing
│   ├── tests.py         # Test cases
│   └── admin.py         # Admin panel configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template with styling
│   ├── home.html        # Main TODO list page
│   └── edit_todo.html   # Edit TODO page
├── db.sqlite3           # SQLite database
└── manage.py            # Django management script
```

## Homework Questions & Answers

This project was built as part of the AI Dev Tools Zoomcamp homework. Here are the answers:

1. **Q1: Install Django** → `pip install django`
2. **Q2: Project and App** → `settings.py`
3. **Q3: Django Models** → Run migrations
4. **Q4: TODO Logic** → `views.py`
5. **Q5: Templates** → `TEMPLATES['DIRS']` in project's settings.py
6. **Q6: Tests** → `python manage.py test`

## Usage

### Creating a TODO
1. Fill in the form on the homepage
2. Add title (required), description (optional), and due date (optional)
3. Click "Add TODO"

### Editing a TODO
1. Click the "Edit" button on any TODO
2. Modify the fields
3. Click "Save Changes"

### Marking as Complete
1. Click "Mark Done" to mark a TODO as resolved
2. Click "Unresolve" to mark it as pending again

### Deleting a TODO
1. Click the "Delete" button
2. Confirm the deletion

## Testing

Run the test suite to verify all functionality:
```bash
python manage.py test
```

Tests cover:
- Model creation and validation
- View functionality
- CRUD operations
- Resolved status toggling


## Contributing

This is a homework project, but feel free to fork and experiment!

## License

This project is for educational purposes.

## Acknowledgments

- Built as part of the AI Dev Tools Zoomcamp
- Created with AI-assisted development using Claude
