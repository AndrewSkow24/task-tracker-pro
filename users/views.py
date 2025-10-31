from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.all()

    # def list(self, request, *args, **kwargs):
    #     # возвращаем только текущего пользователя
    #     serializer = self.get_serializer(request.user)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     #         Запрещаем просмотр других пользоватлей
    #     if int(kwargs["pk"]) != request.user.pk:
    #         return Response(
    #             {"detail": "Доступ запрещён"}, status=status.HTTP_403_FORBIDDEN
    #         )
    #     return super().retrieve(request, *args, **kwargs)
