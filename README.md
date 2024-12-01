# TODO list Project
> Tall you need to do is here

Information about tasks that need to be completed  (tasks by the tags)

## Installing

Python3 must be already installed

```shell
git clone https://github.com/zazmarga/todo_list
cd todo_list
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver  # starts Django server
```

## Features

* You can add tags and tasks, set deadlines
* You can adjust tags and tasks
* Mark completed or not completed tasks
