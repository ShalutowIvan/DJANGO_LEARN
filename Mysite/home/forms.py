from django import forms
from .models import *
from django.core.exceptions import ValidationError


# class AddPostForm(forms.Form):#написали название класса (его можно писать любое) и родителя указали класс Form
#     title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TextInput(attrs={'class': 'form-input'}))#далее тут идут поля которые будут отображаться в нашей форме. Их нужно будет заполнять пользователю. Эти атрибуты совпадают с названиеми полей в модели БД, так как потом эти данные будут попадать в БД. Названия лучше делать такими же как в модели, чтобы облегчить написание кода.
#     slug = forms.SlugField(max_length=255, label="URL")#по сути тут в каждом поле указан тип данных, то есть класс
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label="Контент")
#     is_published = forms.BooleanField(label="Публикация", required=False, initial=True)#сделали поле не обязательным с помощью параметра required. initial означает что по умолчанию будет отмечен этот пункт
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана")#только тут у нас идет запрос из БД категорий и будет выведен выпадающий список. empty_label это надпись для пустого поля

#полный список типов данных для полей формы есть в документации. далее перейдем в файл addpage.html и допищем туда функционал нашей формы.

class AddPostForm(forms.ModelForm):#унаследуем другой базовый класс
    #как написать надпись категории не выбраны в выпадающем списке. Для этого напишем инициализатор. Когда форма отображается, то создается экземпляр класса AddPostForm и вызыввается конструктор, потом вызывается конструктор базового класса, и далее в свойство объекта self.fields['cat'].empty_label записываем значение "Категория не выбрана".
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    #в классе пишем мета класс.
    class Meta:
        model = Home#делаем связь с классом модели
        # fields = '__all__'#пишем какие поля связываем, в нашем случае __all__ означет все поля кроме заполняемы автоматически. Но лучше указывать явный список названий полей. 
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']#указали все кроме фото
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }#тут указали виджет, это стиль оформления для html страницы

    #теперь форма работает также, и появился метод save, который сохраняем данные в БД. Перейдем в файл views.py и перепишем фунцию add_page. 


    def clean_title(self):#этот метод для проверки поля title
        title = self.cleaned_data['title']#из объекта класса AddPostForm получаем свойство cleaned_data, оно там есть так как теняется из базового класса ModelForm, потом его проверяем. 
        if len(title) > 200:#будет сгенерировано исключение в случае если длина поля более 200 символов
            raise ValidationError('Длина превышает 200 символов')#ValidationError нужно также импортировать из django.core.exceptions 
        #в случае если проверка пройдет, то просто возвращается заголовок
        return title

