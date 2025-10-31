from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class Task(models.Model):
    PRIORITY_CHOICES = [("low", "Низкий"), ("medium", "Средний"), ("high", "Высокий")]
    STATUS_CHOICES = [
        ("todo", "Сделать"),
        ("in_progress", "В процессе"),
        ("done", "Завершено"),
    ]
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, verbose_name="Приоритет"
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="todo", verbose_name="Статус"
    )
    due_date = models.DateTimeField(verbose_name="Дата завершения")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks", verbose_name="Проект"
    )
    assignee = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="assigned_tasks",
        verbose_name="Исполнитель задачи",
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_tasks",
        verbose_name="Создатель задачи",
    )

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата и время создания"
    )
    updated_at = (
        models.DateTimeField(auto_now=True, verbose_name="Дата и время выполнения"),
    )
    is_completed = models.BooleanField(default=False, verbose_name="Задача выполнена")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"
