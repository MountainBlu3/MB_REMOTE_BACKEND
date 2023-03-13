from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.staff_registration_view, name='register'),
    path('login/', views.staff_login_view, name='login'),
    # path('logout/', views.staff_logout_view, name='logout')
]
