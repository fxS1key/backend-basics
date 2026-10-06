from dataclasses import dataclass
from datetime import date

from src.exceptions import TaskNotFoundError


@dataclass
class Task:
    id: int
    title: str
    description: str
    due_date: date


def create_task(
    tasks_by_id: dict[str, Task],
    title: str,
    description: str,
    due_date: date,
) -> Task:
    task_id = max(tasks_by_id, default=0) + 1

    task = Task(task_id, title, description, due_date)
    tasks_by_id[task_id] = task
    print(f"Created task task_id={task_id}")
    return task


def get_task_by_id(
    tasks_by_id: dict[str, Task],
    task_id: int,
) -> Task:
    if task_id not in tasks_by_id:
        raise TaskNotFoundError(task_id)
    return tasks_by_id[task_id]
