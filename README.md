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
## Project wiew:

### Home page:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/b68dd432-773f-4365-b463-1dabb3665fa0)
![image](https://github.com/MaksNochvai/todo-list/assets/123680608/8a79e656-3f5f-45a5-aa94-16ed37cab3db)

### Create/Update task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/623f12c7-4d24-4ce9-93e8-4ce00a45f04e)

### Delete task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/6420b75f-4125-4002-b853-51551909eb70)

### Mark complete task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/3627fd75-491c-494c-bf78-5bfc5670640b)
![image](https://github.com/MaksNochvai/todo-list/assets/123680608/01e6310f-3ad3-49be-a861-0761123f60cc)

### Tags page:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/e9c36807-e2ae-4991-877a-be9aecfc06e8)

### Create/Update tags:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/df424c92-24de-457b-99a3-d8521212d9f9)

### Delete tag:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/83fb0679-1874-42bf-8b35-a58b5f2c0d7a)

## Happy TODO listing! 📝
