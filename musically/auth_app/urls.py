from django.urls import path

from musically.auth_app.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileDeleteView, \
    ProfileDetailView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('delete/', ProfileDeleteView.as_view(), name='delete profile'),
    path('details/', ProfileDetailView.as_view(), name='details profile'),
)