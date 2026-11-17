# # вызвать класс CreateView можно прямо в файле urls.py,
# # а все нужные атрибуты передать аргументами в метод as_view():

# # project/urls.py

# # Добавьте новые строчки с импортами классов.
# from django.contrib.auth.forms import UserCreationForm
# from django.views.generic.edit import CreateView
# ...
# # К импортам из django.urls добавьте импорт функции reverse_lazy
# from django.urls import include, path, reverse_lazy

# urlpatterns = [
#     ...
#     path(
#         'auth/registration/', 
#         CreateView.as_view(
#             template_name='registration/registration_form.html',
#             form_class=UserCreationForm,
#             success_url=reverse_lazy('pages:homepage'),
#         ),
#         name='registration',
#     ),
#     ...
# ] 



# # Создайте шаблон registration/registration_form.html и перенесите в него код из листинга:

# {% extends "base.html" %}
# {% load django_bootstrap5 %}

# {% block content %}
#   <div class="card col-4 m-3">
#     <div class="card-header">
#       Регистрация пользователя
#     </div>
#     <div class="card-body">
#       <form method="post">
#         {% csrf_token %}
#         {% bootstrap_form form %}
#         {% bootstrap_button button_type="submit" content="Зарегистрироваться" %}
#       </form>
#     </div>
#   </div>
# {% endblock %} 


# # Можно проверить работу формы регистрации. Откройте страницу http://127.0.0.1:8000/auth/registration/
# # Зарегистрируйтесь как новый пользователь. После регистрации вас переадресует на главную страницу приложения.







# # Если пишем отдельное приложение под кастомного юзера, то форму наследуем от кастомной модели, но методы сохраняем
# # # users/forms.py
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import get_user_model

# # Получаем модель пользователя:
# User = get_user_model()


# class CustomUserCreationForm(UserCreationForm):

#     # Наследуем класс Meta от соответствующего класса родительской формы.
#     # Так этот класс будет не перезаписан, а расширен.
#     class Meta(UserCreationForm.Meta):
#         model = User 






# # Добавим ссылки на новые страницы в навигацию.

# <!-- templates/includes/header.html -->
# <header>
#   <nav class="navbar shadow-sm">
#     <div class="container">
#       {% with request.resolver_match.view_name as view_name %}
#         <ul class="nav nav-pills">
#           <li class="nav-item">
#             <a class="nav-link {% if view_name == 'pages:homepage' %} active {% endif %}"
#               href="{% url 'pages:homepage' %}">
#               Главная
#             </a>
#           </li>
#           <li class="nav-item">
#             <a class="nav-link {% if view_name == 'birthday:create' %} active {% endif %}"
#               href="{% url 'birthday:create' %}">
#               Калькулятор дней рождения
#             </a>
#           </li>
#           <li class="nav-item">
#             <a class="nav-link {% if view_name == 'birthday:list' %} active {% endif %}" href="{% url 'birthday:list' %}">
#               Cписок дней рождения
#             </a>
#           </li>
#           {% if user.is_authenticated %}
#             <span class="navbar-text">Пользователь: <b>{{ user.username }}</b></span>
#             <!-- Новая кнопка -->
#             <li class="nav-item">
#               <a class="nav-link{% if view_name == 'password_change' %} active {% endif %}"
#                 href="{% url 'password_change' %}">Изменить пароль</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="{% url 'logout' %}">Выйти</a>
#             </li>
#           {% else %}
#             <li class="nav-item">
#               <a class="nav-link{% if view_name == 'login' %} active {% endif %}" href="{% url 'login' %}">Войти</a>
#             </li>
#             <!-- Новая кнопка -->
#             <li class="nav-item">
#               <a class="nav-link{% if view_name == 'registration' %} active {% endif %}" href="{% url 'registration' %}">Регистрация</a>
#             </li>
#           {% endif %}
#         </ul>
#       {% endwith %}
#     </div>
#   </nav>
# </header> 