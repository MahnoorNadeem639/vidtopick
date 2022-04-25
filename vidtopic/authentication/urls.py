from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('auth/', views.mainvid, name='mainvid'),
    path('alogin/', views.afterlogin, name='afterlogin'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('history/', views.history, name='history'),
    path('favorites/', views.favorites, name='favorites'),
    path('login/', auth_view.LoginView.as_view(template_name='authentication/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='authentication/logout.html'), name="logout"),
    path('password-reset/',
         auth_view.PasswordResetView.as_view(
             template_name='authentication/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_view.PasswordResetDoneView.as_view(
             template_name='authentication/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_view.PasswordResetConfirmView.as_view(
             template_name='authentication/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_view.PasswordResetCompleteView.as_view(
             template_name='authentication/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]