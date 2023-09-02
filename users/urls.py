from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path

import users.views

app_name = 'users'
urlpatterns = [
    # les liens pour l'application utilisateur
    path('login', users.views.login_user, name="login"),
    # Password reset
    path('change-password/', PasswordChangeView.as_view(
        template_name='registration/password_change_form.html', success_url='done'),
         name='password_change'
         ),
    path('change-password/done/', PasswordChangeDoneView.as_view(
        template_name='registration/password_change_done.html'),
         name='password_change_done'
         ),
    path('profile/', users.views.profile_user, name="profile"),
    #path('profile_pro/', users.views.profile_pro, name="profile_pro"),
    path('logout/', users.views.logout_user, name="logout"),
    #path('registre/', users.views.registre, name="registre"),
    path('registre/',users.views.registreNormalUser, name="registre"),
    #path('registre/pro-user/', users.views.registreProUser, name="pro-registre"),
    path('activate/<uidb64>/<token>', users.views.activate, name='activate'),

]
