import json
from typing import List

from Laba2_task.src.Task import Task
from Laba2_task.src.TaskSource import TaskSource


class FileTaskSource:
    """
    Читает задачи из Json файла
    """
    def __init__(self, filename:str)->None:
        self.filename = filename

    def get_tasks(self) -> List[Task]:
        """
        Читает задачи из JSON файла и преобразует их в объекты Task
        Returns:List[Task]: Список задач из файла или пустой список в случае ошибки
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            tasks = []
            for item in data:
                try:
                    task = Task(id=item["id"],description=item.get("description", ""),priority=item.get("priority", "medium"),status=item.get("status", "pending")
                    )
                    tasks.append(task)
                except Exception:
                    continue
            return tasks
        except FileNotFoundError:
            print("Файл не найден")
            return []
        except json.JSONDecodeError:
            print("Файл не формата JSON")
            return []
        except Exception as e:
            print("Ошибка",e)
            return []
