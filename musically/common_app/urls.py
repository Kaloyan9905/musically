from django.urls import path

from musically.common_app.views import home_page, start_page, custom_404_view

urlpatterns = (
    path('', start_page, name='start page'),
    path('home/', home_page, name='home page'),
)


handler404 = custom_404_view
