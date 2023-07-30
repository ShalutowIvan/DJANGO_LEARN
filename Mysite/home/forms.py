from django import forms
from .models import *


class AddPostForm(forms.Form):#написали название класса (его можно писать любое) и родителя указали класс Form
    title = forms.CharField(max_length=255, label="Заголовок")#далее тут идут поля которые будут отображаться в нашей форме. Их нужно будет заполнять пользователю. Эти атрибуты совпадают с названиеми полей в модели БД, так как потом эти данные будут попадать в БД. Названия лучше делать такими же как в модели, чтобы облегчить написание кода.
    slug = forms.SlugField(max_length=255, label="URL")#по сути тут в каждом поле указан тип данных, то есть класс
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
    is_published = forms.BooleanField(label="Публикация", required=False, initial=True)#сделали поле не обязательным с помощью параметра required. initial означает что по умолчанию будет отмечен этот пункт
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")#только тут у нас идет запрос из БД категорий и будет выведен выпадающий список. empty_label это надпись для пустого поля

#полный список типов данных для полей формы есть в документации. далее перейдем в файл addpage.html и допищем туда функционал нашей формы.
