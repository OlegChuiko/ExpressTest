from django.contrib.auth import views as auth_views
from users.views import CustomPasswordReset
from django.urls import reverse_lazy
from django.urls import path
from users import views


app_name = 'user'

urlpatterns = [
    path('login/',views.Authentication.login,name='login'),
    path('registration/',views.Authentication.registration,name='registration'),
    path('logout/',views.Authentication.logout,name='logout'),

    path('password-reset/', CustomPasswordReset.as_view(), name='password_reset'),   

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='main/password_reset_confirm.html',
        success_url=reverse_lazy('user:password_reset_complete')), name='password_reset_confirm'),

    path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name='password_reset_complete'),
]