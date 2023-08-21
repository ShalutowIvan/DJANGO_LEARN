from django.urls import path, re_path#обяз нужно импортировать функцию path из пакета джанго

from .views import *#импортируем все функции представления из файла views, это функции для ссылок нашего приложения.
#потом делаем список ссылок urlpatterns
urlpatterns = [
	path('', HomeHome.as_view(), name='main'),#этот маршрут будет соответствовать ссылке http://127.0.0.1:8000/home/, это происходит потому что мы его указали в пакете конфигурации urls.py в папке с проектом. Мы переделали начальную ссылку в корневом файл urls, поэтому теперь все ссылки начинаются с доменного имени, home писать не нужно
	# path('cats', categories),#тут будет http://127.0.0.1:8000/home/cats. То есть корневая ссылка берется из файла urls.py в папке с проектом и добавляются тут другие ссылки. Мы переделали начальную ссылку в корневом файл urls, поэтому теперь все ссылки начинаются с доменного имени, home писать не нужно
	# path('cats/<int:catid>/', categories),#теперь если после cats прописать цифру, то страница будет открываться по нумерации. Также этот числовой параметр нужно прописать в файле views.py нашего приложения, не проекта, а приложения.
	# path('cats/<slug:cat>/', categories)
	# path('chan/<slug:chang>/', changes),#http://127.0.0.1:8000/home/chan
	# re_path(r'^archive/(?P<year>[0-9]{4})/', archive)#тут мы пишем, что должен идти префикс archive и год состоящий из 4 цифр и функция обработчик archive. Также в представлениях файл views.py нужно прописать функцию. Ссылка теперь будет. Год должен быть именно из 4-х цифр. Мы переделали начальную ссылку в корневом файл urls, поэтому теперь все ссылки начинаются с доменного имени, home писать не нужно. r стркоа убирает все спец символы в строке, то есть не работают и действуют как обычная строка
	path('about/', about, name='about'),
	path('add_page/', AddPage.as_view(), name='add_page'),
	path('contact/', contact, name='contact'),
	path('login/', LoginUser.as_view(), name='login'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
	path('category/<slug:cat_slug>/', HomeCategory.as_view(), name='category')

]

# handler404 = pageNotFound
#также можно писать и другие ошибки с другими кодами, но только в случае если переменная DEBUG в settings равна False
# handler500
# handler403
# handler400
#документацию можно еще поискать для более подробной инфы


