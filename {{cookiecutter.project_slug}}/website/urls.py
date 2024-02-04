from django.urls import path
from django.contrib.auth import views as auth_views

from website import views

urlpatterns = [
    path("", views.WebsiteView.as_view(), name="website_home"),
    path("dashboard/", views.DashboardView.as_view(), name="website_dashboard"),
    path("register/", views.RegisterView.as_view(), name="website_register_user"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/"),
        name="logout",
    ),
    # path('password_change/', auth_views.PasswordChangeView.as_view(next_page='/'), name='logout'),
]
