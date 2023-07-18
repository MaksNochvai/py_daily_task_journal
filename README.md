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

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/ef85f7ef-b507-4655-acad-40b279b1b970)
![image](https://github.com/MaksNochvai/todo-list/assets/123680608/f0e1d5da-8887-4cdf-aebd-98ca6e4e5f4a)

### Create/Update task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/105f9648-6ab7-4a07-9007-e718be61c34c)

### Delete task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/ae4f1510-c644-4b26-9b34-50eccf1a5361)

### Mark complete task:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/338467a8-61eb-4591-a479-02c76ecc3617)
![image](https://github.com/MaksNochvai/todo-list/assets/123680608/8a464207-ebbd-4c05-b4c2-38d72d11b728)

### Tags page:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/11ada8ff-d508-45e0-8713-145c1f750e3a)

### Create/Update tags:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/c199988d-5dd5-49f8-b105-3c1f8cc5ba1b)

### Delete tag:

![image](https://github.com/MaksNochvai/todo-list/assets/123680608/65b3c5e3-7ce4-4b24-8b53-b678b32573d2)

## Happy TODO listing! 📝
