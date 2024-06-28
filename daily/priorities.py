import datetime
from todoist_api_python.api import TodoistAPI

todoist = TodoistAPI('15140b93826821f4c92819d23fb7cf8ed6a4a859')

todays_date = str(datetime.date.today())

for task in todoist.get_tasks():
    tasks_dictionary = task.to_dict()
    if tasks_dictionary['due'] != None:
        if tasks_dictionary['due']['date'] == todays_date:
            task_id = task.id
            todoist.update_task(task_id=task_id, priority=4)
            print('done')

