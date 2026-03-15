# Dependency Injection Demo

This project is a small Python ToDo application created to demonstrate the Dependency Injection design principle.

## What the program does

The program allows tasks to be added and listed.

The main point of the application is not the ToDo functionality itself, but showing how Dependency Injection works in practice.

The application uses a class called `TodoService`, which depends on a repository for storing tasks.

Two different repository implementations are included:

- `MemoryTaskRepository` stores tasks in memory while the program is running
- `FileTaskRepository` stores tasks in a text file called `tasks.txt`

Because the repository is injected into `TodoService` from outside, the same service class can work with different implementations without being changed.

## How Dependency Injection is used

`TodoService` does not create its own repository.

Instead, the repository is passed into the constructor from `main.py`.

How to run the demo:

1. Make sure Python 3 is installed and working
2. Run the program whit a command "python main.py"

note:
if the application is started multiple times, the `FileTaskRepository` will keep adding the tasks to new lines in the same `tasks.txt`
