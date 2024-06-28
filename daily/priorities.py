import datetime
from todoist_api_python.models import Task
from configurations import *


todoist = connect_todoist()

todays_date = str(datetime.date.today())

for task in todoist.get_tasks():
    tasks_dictionary = task.to_dict()
    if tasks_dictionary['due'] != None:
        if tasks_dictionary['due']['date'] == todays_date:
            task_id = task.id
            todoist.update_task(task_id=task_id, priority=4)
            print('done')

