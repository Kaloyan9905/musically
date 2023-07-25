from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from musically.auth_app.forms import RegisterUserForm, LoginUserForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'common/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('home page')


class LoginUserView(auth_views.LoginView):
    template_name = 'common/login.html'
    form_class = LoginUserForm


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('start page')



