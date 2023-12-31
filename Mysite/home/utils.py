from django.db.models import Count
from django.core.cache import cache#модулья для кеширования на низком уровне


from .models import *

menu = [{'title': "О сайте", "url_name": "about"},
{'title': "Добавить статью", "url_name": "add_page"},
{'title': "Обратная связь", "url_name": "contact"},
# {'title': "Войти", "url_name": "login"}
]


class DataMixin:#сюда мы перенесли метод для формирования шаблона. и словарь с менюшкой вне класса.
    paginate_by = 20
    def get_user_context(self, **kwargs):
        context = kwargs#сохраняем словарь с именованными параметрами в переменную. В шаблоне ранее мы юзали пользовательские теги. Теперь есть метод для этого в отдельном классе. И можно теги не юзать. Тег из шаблона base.html уберем. ТАм был этот тег {% show_categories 'name' cat_selected %}. И пропишем вывод рубрик через коллекцию cats как было раньше то есть перерем в цикле коллекцию cats.  
        # cats = Category.objects.all()#модель также нужно импортировать
        cats = cache.get('cats')#тут мы прочитали коллекцию cats получается из кеша. Ключ назовем "cats"
        if not cats:#если "cats" равно None, то есть данные не прочитаны. То мы их прочитаем как обычно и сделаем кеш.
            cats = Category.objects.annotate(Count('home'))#прописали тут агрегирующую функцию, чтобы скрыть категорию в случае если с это категорией нет домов. Мы тут делаем еще одно свойство для объекта с колвом домов с э\той категорией и шаблоне потом идет проверка на колво записей с этой категорией.
            cache.set('cats', cats, 60)#занесем коллекцию в кеш и укажем время на сколько мы ее будем использовать. Врем яуказывается в секундах.

        # context['menu'] = menu
        # context['cats'] = cats

        # cats = Category.objects.annotate(Count('home'))

        user_menu = menu.copy()#сделали копию меню 
        if not self.request.user.is_authenticated:#тут проверка. Если пользователь не авторизован то идет проверка, is_authenticated это свойств обхекта user. Если свойство принимает значение тру, значит польщзователь авторизован. Если фолз, значит не авторизован. И так как мы написали перед условием not, то значит пользователь не авторизован и мы тогда из меню удаляем элемент с индексом 1, и в меню не будет кнопки для добавления поста.
            user_menu.pop(1)
        context['menu'] = user_menu

        context['cats'] = cats

        if 'cat_selected' not in context:#тут проверка если переменной нет в контексте, значит категория выбрана уже, и значение присваивается 0. Если есть, значит категория не выбрана и значение cat_selected оставляем.
            context['cat_selected'] = 0
        return context


# далее переходим в файл views.py и импортируем все из файла utils.py