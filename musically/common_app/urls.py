from django.urls import path

from musically.common_app.views import home_page, start_page

urlpatterns = (
    path('', start_page, name='start page'),
    path('home/', home_page, name='home page'),
)