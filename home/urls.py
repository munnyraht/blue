from django.contrib.auth import views as authviews
from django.urls import path

urlpatterns = [
	path('loginfrontend/', authviews.LoginView.as_view(), name='loginfrontend'),
    path('logout/', authviews.LogoutView.as_view(), name='logoutfrontend'),

    #Password Reset
    path('password-change/', authviews.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', authviews.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', authviews.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', authviews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authviews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', authviews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]