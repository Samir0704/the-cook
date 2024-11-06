from rest_framework import viewsets
from .models import User, Profession, Certificate, Achievement
from .serializers import UserSerializer, ProfessionSerializer, CertificateSerializer, AchievementSerializer
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

class ProfessionViewSet(ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class CertificateViewSet(ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class AchievementViewSet(ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


class UserViewSet(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer