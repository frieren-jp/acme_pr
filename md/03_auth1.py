# # Подключение urls модуля django.contrib.auth
# # Файл urls.py модуля django.contrib.auth выглядит так:

# # django/contrib/auth/urls.py
# from django.contrib.auth import views
# from django.urls import path


# urlpatterns = [
#     # Логин.
#     path('login/', views.LoginView.as_view(), name='login'), 
#     # Логаут.
#     path('logout/', views.LogoutView.as_view(), name='logout'), 

#     # Изменение пароля.
#     path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#     # Сообщение об успешном изменении пароля.
#     path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#     # Восстановление пароля.
#     path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#     # Сообщение об отправке ссылки для восстановления пароля.
#     path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#     # Вход по ссылке для восстановления пароля.
#     path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     # Сообщение об успешном восстановлении пароля.
#     path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
# ]


# # Подключите файл к головному urls.py проекта:
# # acme_project/urls.py
# ...

# urlpatterns = [
#     ...
#     # Подключаем urls.py приложения для работы с пользователями.
#     path('auth/', include('django.contrib.auth.urls')),
#     ...
# ] 

# # В каталоге templates/, расположенном в корне проекта, создайте директорию registration/,
# # а в ней создайте пустые HTML-файлы для шаблонов:
# └───templates/
#     ├─── ...
#     └─── registration/
#          ├─── logged_out.html
#          ├─── login.html
#          ├─── password_change_done.html
#          ├─── password_change_form.html
#          ├─── password_reset_complete.html
#          ├─── password_reset_confirm.html
#          ├─── password_reset_done.html
#          └─── password_reset_form.html
