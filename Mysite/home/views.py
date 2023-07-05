from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

# Create your views here. 
#имя функции представления может быть любым, мы его определяем сами
def index(request): # тут есть обязательный параметр request, это ссылка на класс HttpRequest. Он содержит информацию о запросе, сессиях куки и тд. Через эту переменную доступна вся инфа в рамках текущего запроса
	return HttpResponse('Страница приложения Home моя хата')#функция должна формировать объекта класса HttpResponse, на выходе формируется объект класса HttpResponse, его также нужно импортировать как модуль (в скобках то что будет содержать главная страница). Теперь нужно связать ее с нужным урл адресом. далее идем в файл url.py в пакет конфигурации проекта, но не приложения, в нашем случае это папка Mysite, там будет список urlpatterns, в него нужно добавить ссылку на функцию из нашего приложения. Теперь идем в файл urls.py. Теперь при запуске сервера будет выводится страница с этим текстом

def categories(request):
	return HttpResponse("<h1>Статьи по категориям</h1>")



# def categories(request, catid):#прописали параметр catid для переъхода по нумерации страниц
# 	# if (request.GET):#сделали проверку, на то что пустой запрос GET или нет
# 	# 	print(request.GET)#вывели словарь из параметров запроса. Сработает это когда мы обратимся к этому представлению. <QueryDict: {'name': ['Gagarina'], 'cat': ['music']}>. Без гет запроса словарь не будет выводиться
# 	# if (request.POST):#можно писать и пост запросы, о них будет речь идти далее
# 	# 	print(request.POST)
# 	return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def changes(request, chang):#прописали параметр chang для переъхода по нумерации страниц с использованием типа slug, чтобы можно было писать строки вместо цифр
	return HttpResponse(f"<h2>Выборки по разделам</h2><p>{chang}</p>")

def archive(request, year):#year потому что его определяли в регулярном выражении, по аналогии как с catid
	# if int(year) > 2023:
	# 	raise Http404()#генерация ошибки с помощью класса/ Если ввести год больше чем 2023, то будет страница не найдена
	if int(year) > 2023:
		return redirect('/', permanent=True)#создали редирект, функцию redirect также нужно импортировать. Если просто слеш написать то мы вернемся на корневую страницу. Без permanent=True будет редирект 302 то есть временный, с permanent=True будет постоянный 301. Эту функцию нужно обязательно возвращать return. Также не желательно прописывать явную страницу редиректа, так как она может измениться и потом будут ошибки 

	return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')#HttpResponseNotFound нужно также импортировать

