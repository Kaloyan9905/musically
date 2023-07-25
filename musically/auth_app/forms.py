from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']
        field_classes = {
            'username': auth_forms.UsernameField,
        }
