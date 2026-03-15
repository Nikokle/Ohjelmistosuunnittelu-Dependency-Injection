# main.py
# Main program for the Dependency Injection demo.
# Here we choose which repository implementation the application will use.

from todo_service import TodoService
from repositories import MemoryTaskRepository, FileTaskRepository


def run_with_memory_repository():
    print("=== ToDo app using MemoryTaskRepository ===")

    # Dependency is created here, outside TodoService
    memory_repo = MemoryTaskRepository()

    # Dependency Injection happens here:
    # TodoService receives its repository from outside
    service = TodoService(memory_repo)

    service.add_task("Buy groceries")
    service.add_task("Finish Dependency Injection report")
    service.add_task("Record teaching video")

    print("Tasks:")
    for task in service.list_tasks():
        print(f"- {task}")


def run_with_file_repository():
    print("\n=== ToDo app using FileTaskRepository ===")

    # Dependency is created here, outside TodoService
    file_repo = FileTaskRepository("tasks.txt")

    # Dependency Injection happens here:
    # TodoService receives its repository from outside
    service = TodoService(file_repo)

    service.add_task("Wash the car")
    service.add_task("Practice Python")
    service.add_task("Push project to GitHub")

    print("Tasks:")
    for task in service.list_tasks():
        print(f"- {task}")


if __name__ == "__main__":
    # Run both examples so it is easy for the teacher to see
    # that the same service works with different implementations.
    run_with_memory_repository()
    run_with_file_repository()