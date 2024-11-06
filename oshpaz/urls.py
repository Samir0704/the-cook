from django.urls import path
from oshpaz.views import ProfessionViewSet,CertificateViewSet,AchievementViewSet,UserViewSet
from oshpaz import auth
urlpatterns = [
    path('proffesion/', ProfessionViewSet.as_view(), name='proffesion'),
    path('certificate/', CertificateViewSet.as_view(), name='certificate'),
    path('achivment/', AchievementViewSet.as_view(), name='achivment'),
    path('user-view/', UserViewSet.as_view(), name='user-view'),
     # Login
    path('user-login/',auth.UserLoginAPIView.as_view(),name = 'login'),
    path('user-register/',auth.UserRegisterAPIView.as_view(), name='register'),
    path('user-logout/',auth.UserLogoutAPIView.as_view(),name = 'logout'),

]