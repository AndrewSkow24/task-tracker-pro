from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

"""
Класс Q из django.db.models предназначен для построения сложных 
SQL-запросов с логическими операторами (OR, AND, NOT), которые 
невозможно (или неудобно) выразить через стандартные аргументы 
метода .filter()
"""
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]

    queryset = Task.objects.all()

    # показываем задачи, где пользователь или создатель или исполнитель
    # def get_queryset(self):
    #     return Task.objects.filter(
    #         Q(creator=self.request.user) | Q(assignee=self.request.user)
    #     ).order_by("-created_at")

    def perform_create(self, serializer):
        # автоматически устанавливает создателя при создании
        serializer.save(creator=self.request.user)

    def destroy(self, request, *args, **kwargs):
        isinstance = self.get_object()
        # instance - это экземпляр модели Django - конкретная запись в БД
        if isinstance.creator != request.user:
            return Response(
                {"detail": "Только создатель может удалить задачу"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)
