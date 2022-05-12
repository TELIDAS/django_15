from django.urls import path
from . import views, models


app_name = "users_urls"
urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),
    path("login/", views.NewLoginView.as_view(), name="login"),
    path("users/", views.UserListView.as_view(), name="users"),
]
