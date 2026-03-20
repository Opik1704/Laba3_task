from datetime import time
import time
from src.Task import Task
from src.TaskSource import TaskSource
from src.FileTaskSource import FileTaskSource
from src.GeneratorTaskSource import GeneratorTaskSource
from src.APITaskSource import APITaskSource

from src.exceptions import TaskPriorityError, TaskIdError


def main():
    """Вход в приложение и создание tasks и вызов методов"""
    task = Task(id="Task1", description="Описание", priority="high")

    print(f"Задача создана: {task}")
    print(task.is_ready)
    print(f"Возраст задачи: {task.age_seconds:.4f} сек")

    task.start()
    print(task.status, task.icon)
    time.sleep(1.1)
    print(task.is_overdue)

    task.complete()
    print(task.is_completed, task.icon)

    try:
        task.priority = "fake"
    except TaskPriorityError as e:
        print(f"Ошибка {e}")

    try:
        task.id = 12345
    except TaskIdError as e:
        print(f"Ошибка {e}")

    print(f"Иконка по умолчанию {task.icon}")
    task.icon = "🔥"
    print(f"Иконка после правки {task.icon}")

    print(f"Текущий приоритет: {task.priority}")
    task.__dict__['priority'] = "fake"
    print(f"Лезем грязными руками {task.priority}")
if __name__ == "__main__":
    main()
