from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("member", "Участник"),
        ("manager", "Менеджер"),
        ("admin", "Администратор"),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="member")

    # Явно указываем related_name для групп и разрешений
    group = models.ManyToManyField(
        "auth.Group",
        verbose_name="Группы",
        blank=True,
        help_text="Группы в которых состоит пользователь",
        related_name="custom_user_groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="Разрешения пользователя",
        blank=True,
        help_text="Индивидуальные разрешения для этого пользователя",
        related_name="custom_user_permissions",
    )
