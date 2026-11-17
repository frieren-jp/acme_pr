from django import forms

# Импортируем класс модели Birthday.
from .models import Birthday


# Для использования формы с моделями меняем класс на forms.ModelForm.
class BirthdayForm(forms.ModelForm):
    # Удаляем все описания полей.

    # Все настройки задаём в подклассе Meta.
    class Meta:
        # Указываем модель, на основе которой должна строиться форма.
        model = Birthday
        fields = ('first_name', 'last_name', 'birthday')
        widgets = {'birthday': forms.DateInput(attrs={'type': 'date'})} 
        
        




 # from django import forms


# class BirthdayForm(forms.Form):
#     first_name = forms.CharField(label='Имя', max_length=20)
#     last_name = forms.CharField(
#         label='Фамилия', required=False, help_text='Необязательное поле'
#     )
#     birthday = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'type': 'date'}))
