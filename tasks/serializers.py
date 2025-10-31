from rest_framework import serializers
from .models import Task

# сериализатор превращает экземпляры моделей или наборы QuerySet
# в простые данные (словари или списки), которые затем можно превратить в JSON

# десериализация - принимает данные из запросов и преобразует их
# обратно в объекты Python


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
