# repositories.py
# This file contains different repository implementations.
# Both repositories provide the same kind of functionality:
# storing tasks and returning them.

import os


class MemoryTaskRepository:
    def __init__(self):
        # Tasks are stored only in memory while the program is running.
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_all_tasks(self):
        return self.tasks


class FileTaskRepository:
    def __init__(self, filename):
        # Tasks are stored in a text file.
        self.filename = filename

        # Create the file if it does not already exist.
        if not os.path.exists(self.filename):
            with open(self.filename, "w", encoding="utf-8") as file:
                pass

    def add_task(self, task):
        # Add a task to the text file, one task per line.
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(task + "\n")

    def get_all_tasks(self):
        # Read all tasks from the file and return them as a list.
        with open(self.filename, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines() if line.strip()]