# todo_service.py
# This file contains the main application logic.

class TodoService:
    def __init__(self, repository):
        # Dependency Injection:
        # TodoService does not create the repository itself.
        # The repository is given from outside.
        self.repository = repository

    def add_task(self, task):
        # This method adds a new task using the injected repository.
        self.repository.add_task(task)

    def list_tasks(self):
        # This method returns all tasks using the injected repository.
        return self.repository.get_all_tasks()