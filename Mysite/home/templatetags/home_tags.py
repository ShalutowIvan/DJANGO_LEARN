from django import template
from home.models import *

register = template.Library()#создали класс для регистрации библиотеки тегов


# @register.simple_tag()#тег для простой функции. Теперь его можно юзать в html шаблонах приложения. Далее идем в base.html и добавим туда наш модуль с функциями тегов
# def get_categories():
# 	return Category.objects.all()#это для возвращения всех записей.

#далее нужно превратить эту функцию в тег. Для этого можно прописать декоратор @register.simple_tag()

@register.simple_tag()
def get_categories():
    return Category.objects.all()

