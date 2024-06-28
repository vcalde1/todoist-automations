import os
from todoist_api_python.api import TodoistAPI


def connect_todoist():
    todoist = TodoistAPI('15140b93826821f4c92819d23fb7cf8ed6a4a859')

    return todoist
