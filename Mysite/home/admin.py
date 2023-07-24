from django.contrib import admin

# Register your models here.
#сначала импортируем все модели из файл models
from .models import *

#потом регистрируем нужную нам модель
admin.site.register(Home)
#теперь в админке появилась наша модель, ее можно просматривать из админки, там будут ссылки на каждую запись БД например. Их можно просматривать как через саму амднку так и есть ссылки на сайт. Для перехода из админки на сам сайт нужно прописывать функцию в модели get_absolute_url. Если ее не прописать, то кнопки не будет. Или если прописать другое название функции, то тоже в админке кнопки не будет. Далее пропишем название модели, чтобы было прописано не просто homes, а так как нам нужно. Перейдем в файл models.py. #прописали внутренний мета класс для указания названия приложения в админке





