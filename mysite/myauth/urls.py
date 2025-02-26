from django.urls import path
from .views import login_view, LogoutView, RegisterView, edit_profile

app_name = "myauth"

urlpatterns = [
    path('login/', login_view, name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path('edit_profile/', edit_profile, name='edit_profile'),
]


