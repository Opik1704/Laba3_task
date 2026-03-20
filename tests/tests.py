import unittest
import os
import json
import tempfile
from src.Task import Task
from src.FileTaskSource import FileTaskSource
from src.descriptors import IdDescriptor, PriorityDescriptor, StatusDescriptor
from src.exceptions import TaskPriorityError, TaskIdError, TaskStateError, TaskDescriptionError,TaskStatusError


class TestDescriptors(unittest.TestCase):
    """Тестирование дескрипторов и методов"""

    def test_valid_priority(self):
        """Проверка правильных приоритетов"""
        for p in ["low", "medium", "high", "critical"]:
            with self.subTest(priority=p):
                task = Task(id="test", description="desc", priority= p )
                self.assertEqual(task.priority, p)

    def test_invalid_priority_raises(self):
        """Проверка неправильного приоритета"""
        with self.assertRaises(TaskPriorityError):
            Task(id="test", description="desc", priority="fake")

        with self.assertRaises(TaskPriorityError):
            Task(id="test", description="desc", priority=123)

    def test_status_icon_logic(self):
        """Проверка иконок (Non-Data дескриптора)"""
        task = Task(id="T1", description="Test", priority="medium")
        self.assertEqual(task.icon, "⏳")

        task.start()
        self.assertEqual(task.icon, "🚀")

        task.complete()
        self.assertEqual(task.icon, "✅")

    def test_state_transitions(self):
        """Проверка статуса"""
        task = Task(id="T1", description="Test", priority="low")
        with self.assertRaises(TaskStateError):
            task.complete()

    def test_task_time_properties(self):
        """Проверка времени"""
        task = Task(id="T_TIME", description="Time test", priority="low")
        self.assertGreaterEqual(task.age_minutes, 0)
        self.assertGreaterEqual(task.age_hours, 0)

    def test_task_overdue_logic(self):
        """Проверка is_overdue"""
        task = Task(id="T_OVERDUE", description="Overdue test", priority="medium")
        self.assertFalse(task.is_overdue)

    def test_task_cancel_logic(self):
        """Проверка отмены задачи"""
        task = Task(id="T_CANCEL", description="Cancel test", priority="high")
        task.start()
        task.cancel()
        self.assertEqual(task.status, "pending")

    def test_descriptor_class_access(self):
        """Проверка доступа через класс """
        self.assertIsInstance(Task.id, IdDescriptor)
        self.assertIsInstance(Task.priority, PriorityDescriptor)

    def test_invalid_description_type(self):
        """Проверка  описания"""
        task = Task(id="T_DESC", description="Desc", priority="low")
        with self.assertRaises(TaskDescriptionError):
            task.description = 1000

class TestTaskSources(unittest.TestCase):
    """Проверка получение задачи """
    def test_list_source_success(self):
        """Проверка создания задач из обычного списка словарей."""
        data = [
            {"id": "1", "description": "first", "priority": "low"},
            {"id": "2", "description": "Second", "priority": "high"}
        ]
        tasks = [Task(**item) for item in data]

        self.assertEqual(len(tasks), 2)
        self.assertEqual(tasks[1].priority, "high")
        self.assertEqual(tasks[0].id, "1")

    def test_bad_source(self):
        """Неправмильную задачу передали """
        data = [
            {"id": "1", "description": "Good", "priority": "low"},
            {"id": "2", "description": "Bad", "priority": "fake"}
        ]
        tasks = []
        for item in data:
            try:
                tasks.append(Task(**item))
            except (TaskPriorityError, TaskIdError, TaskDescriptionError):
                continue

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].id, "1")

    def test_file_source_empty_if_no_file(self):
        """Отсутвие файла"""
        source = FileTaskSource("not_exists.json")
        self.assertEqual(source.get_tasks(), [])


if __name__ == "__main__":
    unittest.main()