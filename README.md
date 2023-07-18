# TODO List Project

-----------------------------------

This is a simple TODO List web application developed using Django. The application allows users to create tasks, mark them as completed, and add tags to tasks for better organization.

## Installing using GitHub

-----------------------------------

1. Clone the repository: https://github.com/MaksNochvai/todo-list
2. Set up a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate # Activation of the virtual environment (Unix)
venv\Scripts\activate # Activation of the virtual environment (Windows)
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Migrate in db:
```
python manage.py migrate
```
5. Input your secret key and Debug status in .env.sample:
```
SECRET_KEY=YOUR_SECRET_KEY
DEBUG=YOUR_DEBUG_STATUS
```
6. Load the initial data (optional):
  
    If you want to load some initial data for tasks and tags, you can use Django fixtures. Create JSON fixture files as shown in the previous section and load them:
```
python manage.py loaddata tasks.json
python manage.py loaddata tags.json
```
7. Run Server:
```
python manage.py runserver
```

----------------------
## Features
- Create new tasks with a description and an optional deadline.
- Mark tasks as completed and view completed tasks separately.
- Add tags to tasks to categorize and organize them.
- Edit and delete existing tasks and tags.
- Pagination for better navigation.

---------
