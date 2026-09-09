from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from apps.testapp.permissions import IsAdminOnly, IsModeratorOrAdmin, IsUserOnly


# Эндпоинт 1: Доступен ЛЮБОМУ авторизованному юзеру
class PublicDataView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Привет, {request.user.email}! Это обычные данные."})


# Эндпоинт 2: Доступен ТОЛЬКО Модераторам и Админам
class SecretModeratorView(APIView):
    permission_classes = [IsModeratorOrAdmin]

    def get(self, request):
        return Response({"message": f"Секретная панель! Твоя роль: {request.user.role}."})





class AdminPanelAPIView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        return Response({"message": f"Добро пожаловать в панель администратора!"})

class UserDashboardAPIView(APIView):
    permission_classes = [IsUserOnly]

    def get(self, request):
        return Response({"message": f"Личный кабинет пользователя!"})
