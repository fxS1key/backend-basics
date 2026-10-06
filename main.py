from datetime import date

from src.services import Task, create_task, get_task_by_id


def main() -> None:
    tasks_by_id: dict[str, Task] = {}
    task = create_task(
        tasks_by_id,
        "README",
        "Добавить раздел 'запуск'",
        date(2026, 3, 23),
    )

    print(get_task_by_id(tasks_by_id, task.id))
    print(get_task_by_id(tasks_by_id, 3))


if __name__ == "__main__":
    main()
