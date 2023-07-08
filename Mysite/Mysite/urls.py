"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# from home.views import index, categories
from home.views import *
from django.urls import path, include
from Mysite import settings

#тут нужно добавить маршрут. Пока тут только обращение к админке 
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', index),#указали свою ссылку, название приложения и потом ссылка для активации запроса, то есть ссылку на функцию, которую нужно предварительно импортировать из файла home.views. Также можно поменять рабочий каталог. Для этого нужно нажать ПКМ на папку с проектом, потом выбрать Mark Directiry as далее Sources Root. По факту теперь префикс home/ будет добавляться к домену нашего сайта http://127.0.0.1:8000/home так будет выглядеть ссылка 
    # path('cats/', categories),#cats это шаблон, и теперь можно будет перейти по ссылке http://127.0.0.1:8000/cats/
    # path('', index)#теперь на главной странице тоже будет функция представления index
    # path('home/', include('home.urls'))#теперь ко всем адресам будет добавляться префикс home/ а сами адреса будут подтягиваться из модуля urls из папки home то есть из папки с нашим приложением. Получается вставляем сразу все ссылки которые будут в нашем приложении. Файл нужно будет создать если его нет в нашем пакете нашего приложения.
    path('', include('home.urls'))#теперь все адреса будут начинаться от доменного имени, то есть от IP 
]
# также как только мы добавили ссылку, то теперь старовая страница которая открывается через IP и порт будет выдавать ошибку 404. к ней тоже можно прописать маршрут

# можно также сделать папку с приложением сделать рабочим каталогом. в пайчарме для нужно нажать пкм на папку и выбрать mark Dicretory as, потом  Source Root. Либо можно этого не делать
# этот префикс 'home/' в итоге будет добавляться к домену нашего сайта. 
# Будет такая ссылка: http://127.0.0.1:8000/home - по этому маршруту будет активизироваться функция index
# остановился на 12 минут 2 урок

# также можно указывать и список маршрутов приложения from django.urls import path, include. А все остальные ссылки path можно убрать. Префикс будет тянуться из папки с проектом

# убрали ссылку на приложение, теперь все маршруты будут идти от доменного имени



if settings.DEBUG:#в случае включенного режима дебага то есть DEBUG=True мы к маршрутам urlpatterns которые мы указали выше добавляем маршрут для статических данных графических файлов и указываем наш добавленный урл и корневую папку где будут храниться файлы, скорее всего static это функция такая. Делается это только в отладочном режиме, на реальных серверах это уже настроено, но у нас не настроено. static надо импортировать из django.conf.urls.static. DEBUG должен быть True. Теперь тестовый сервер может их брать по адресу media и отображать на html странице
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




handler404 = pageNotFound#эту функцию нужно импортировать из папки с приложением из файла views.py