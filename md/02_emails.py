# # Рассмотрим простейший случай: отправку обычного текстового письма.
# # Такие письма отправляются с помощью функции send_mail() из модуля django.core.mail:

# # Импорт функции для отправки почты.
# from django.core.mail import send_mail

# # Пример вызова функции:
# send_mail(
#     subject='Тема письма',          
#     message='Текст сообщения',  
#     recipient_list=['to@example.com'],
#     fail_silently=True,
# ) 


# # В функцию send_mail() передаются обязательные параметры subject, message, from_email и recipient_list:
# subject:  #тема письма (строка).
# message:  # текст сообщения (строка).
# from_email:  # от кого (строка); если аргумент не указан — Django возьмёт значение параметра DEFAULT_FROM_EMAIL из настроек проекта.
# recipient_list:  # адреса получателей (список строк). Получатели увидят, кому ещё было отправлено это письмо: адреса всех получателей отобразятся в поле «Кому».
# fail_silently:  # необязательный аргумент. Если для этого аргумента установлено значение True,
# # то ошибка отправки письма не вызовет ошибки приложения.


# # Для эксперимента настроим почтовые уведомления для администратора сайта — будем отправлять ему письмо всякий раз, когда кто-то представляется именем одного из участников группы “The Beatles”.
# # Добавьте в birthday/forms.py код для отправки письма администратору:
# #  birthday/forms.py
# ...
# # Импорт функции для отправки почты.
# from django.core.mail import send_mail

# BEATLES = {'Джон Леннон', 'Пол Маккартни', 'Джордж Харрисон', 'Ринго Старр'}


# class BirthdayForm(forms.ModelForm):

#     ...

#     def clean(self):
#         super().clean()
#         first_name = self.cleaned_data['first_name']
#         last_name = self.cleaned_data['last_name']
#         if f'{first_name} {last_name}' in BEATLES:
#             # Отправляем письмо, если кто-то представляется 
#             # именем одного из участников Beatles.
#             send_mail(
#                 subject='Another Beatles member',
#                 message=f'{first_name} {last_name} пытался опубликовать запись!',
#                 from_email='birthday_form@acme.not',
#                 recipient_list=['admin@acme.not'],
#                 fail_silently=True,
#             )
#             raise ValidationError(
#                 'Мы тоже любим Битлз, но введите, пожалуйста, настоящее имя!'
#             )
        
# # Запустите проект и отправьте через форму имя любого участника Beatles.
# # Если всё настроено правильно, то в корневой директории в папке /sent_mails появится текстовый файл с письмом

