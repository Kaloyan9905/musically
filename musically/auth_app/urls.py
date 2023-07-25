from django.urls import path

from musically.auth_app.views import RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
)