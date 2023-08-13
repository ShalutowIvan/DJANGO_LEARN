from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView


from .forms import *
from .models import *


# Create your views here. 
#имя функции представления может быть любым, мы его определяем сами
# def index(request): # тут есть обязательный параметр request, это ссылка на класс HttpRequest. Он содержит информацию о запросе, сессиях куки и тд. Через эту переменную доступна вся инфа в рамках текущего запроса
# 	return HttpResponse('Страница приложения Home!!!!!!!!!')#функция должна формировать объекта класса HttpResponse, на выходе формируется объект класса HttpResponse, его также нужно импортировать как модуль (в скобках то что будет содержать главная страница). Теперь нужно связать ее с нужным урл адресом. далее идем в файл url.py в пакет конфигурации проекта, но не приложения, в нашем случае это папка Mysite, там будет список urlpatterns, в него нужно добавить ссылку на функцию из нашего приложения. Теперь идем в файл urls.py. Теперь при запуске сервера будет выводится страница с этим текстом

#перепишем функцию index с шаблонизатором render
# menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']
menu = [{'title': "О сайте", "url_name": "about"},
{'title': "Добавить статью", "url_name": "add_page"},
{'title': "Обратная связь", "url_name": "contact"},
{'title': "Войти", "url_name": "login"}
]


class HomeHome(ListView):#создали класс списка представлений
	model = Home#сделали ссылку на модель Home. Эта запись ссылается на модель и будет отображать список статей из модели Home. То есть выбирает все записи из таблицы и отображает их в виде списка. ListView использует шаблон <имя приложения>/<имя модели>_list.html. И строка model = Home будет отображать список всех записей из таблицы home и отображать их в шаблоне <имя приложения>/<имя модели>_list.html, то есть имя шаблона по умолчанию будет home_list.html, но этот шаблон можно и самим прописать. . То есть получается наша запись заменяет уже функцию index. Также этот класс нужно прописать в url.py. Там нужно вместо функции index написать HomeHome.as_view() именно со скобками, а не без скобок. Пропишем наш шаблон index.html, чтобы этот класс не ссылался на стандартный шаблон.
	template_name = 'home/index.html'
	#страница будет пустая. Так как у нас в функции передавался список posts, а теперь его нет. В классе ListView по умолчанию используется свой список объектов object_list. Теперь если posts заменить на object_list , то все заработает. Но можно и прописать свой список строк таблицы
	context_object_name = 'posts'#прописали наш список
	#теперь нужно добавить заголовок
	# extra_context = {'title': 'Главная страница'}#extra_context в не можно указывать только неизменяемые данные. Список туда нельзя указать. Для этого нужно создать специальную функцию get_context_data

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)#сначала нужно получить контекст который уже сформирован для нашего шаблона. Мы его записали в переменную используея базовый шаблон. Например коллекция posts уже есть и ее нельзя удалять. То есть мы тут берем базовый класс ListView и в функцию для выборки контекста передает все именованные параметры, распаковываем словарь, так как все данные тут передаются словарями. Теперь в этом словаре мы можем менять или прописывать какие-то другие атрибуты. Можно формировать и новые ключи.
		context['menu'] = menu#теперь мы создали новый словарь в контектсте и присвоили ему наше меню, которое мы указали сверху вне класса.
		context['title'] = 'Главная страница'
		context['cat_selected'] = 0#это чтобы ссылка пропадала при нажатии на раздел категории
		return context#и контекст обязательно нужно возвращать.
	#еще можно сделать так чтобы из таблицы выбирались не все записи, а например только опубликованные, то есть получается фильтр можно сделать. Для этого нужно дполнительно прописать функцию get_queryset и указать в ней фильтр.

	def get_queryset(self):
		return Home.objects.filter(is_published=True)#будут выведены только те статьи которые опубликованы. Далее пропишем класс для функци отображения категорий.


# def index(request):
# 	posts = Home.objects.all()#считали все записи из БД и сохранили ее в переменную posts и его нужно передать в словарь в функции render. В html файлах через шаблонизатор мы также перебираем наш список posts, и так как каждый элемент списка это объект со свойствами мы там обращаемся к свойставам объекта в цикле и все на странице отображается. Также фреймворк джанго через функцию all подключается к БД и отключается, больше ничего писать тут не нужно
# 	# cats = Category.objects.all()#считали записи из таблицы категории
# 	context = {
# 		"posts": posts,
# 		# 'cats': cats,
# 		"menu": menu,
# 		'title': 'Главная страница',
# 		'cat_selected': 0#далее модифицируем функцию show_categories, чтобы отображать статьи по отдельным рубрикам.
# 	}#так прописывать правильнее, так как это выглядит более наглядно
# 	return render(request, "home/index.html", context=context)#тут вместо объекта класса HttpResponse пишем функцию render, в качестве параметра пишем request это ссылка на объект Hhttprequest, далее вторым параметром пропишем путь к шаблону. Шаблоны нужно хранить в папке templates, эту папку нужно создать в папке с приложением для которого будем делать шаблоны. Но есть один момент, когда мы будем дальше хостить наш проект, то все шаблоны со все приложений будут сохраняться в единой папке templates нашего проекта, то есть в папке приложений, а в папке проекта все шаблоны могут быть, и там могут совпадать имена файлов. Поэтому в папке templates приложения нужно создать папку с названием приложения и туда сохранять шаблоны. Тогда при сборке всего проекта подкаталог с имененем приложения (home в нашем случае) перенесется в папку templates, и уже не перепутаются имена файлов. Создадим файл index.html в этой папку home с кодировкой UTF-8, это важно, так как питон ее использует. Теперь укажем путь к файлу шаблону. ПУть полный писать не нужно, просто пишем название приложения и название файла html, пишем так, потому что в файле settings.py в папке проектом прописана конфигурация, там есть коллекция TEMPLATES, там есть описание где будут искаться шаблоны. То есть джанго ищет шаблоны в папке templates, а путь в этой папке мы как раз и прописываем во втором параметре
#теперь функция render возвращает содержимое файла index.html






def about(request):
	return render(request, "home/about.html", {"menu": menu, 'title': 'О приложении'})
#так в самом простом виде можно добавлять шаблоны html страниц. Также там можно прописывать шаблоны самим, но их нужно прописывать в функции render третьим аргументом в виде словаря, а html файле прописывать название переменной в двух фигурных скобках
# Сделаем меню на главной странице. Для этого сделаем список из строк для нашего меню
#и добавим этот список как второй элемент словаря в третьем параметре в функции render
#на вторую страницу тоже добавили этот же список меню. Теперь получается мы нарушили принцип DRY (не повторяться). Для этого можно создать базовый шаблон для представления страниц на сайте в целом, а уже потом можно его расширить другими шаблонами. Код шаблонов можно посмотреть в файлах, там также можно писать циклы питона и перебирать наши списки из питона и тд. В других страницах мы просто как бы дописвваем базову страницу новым содержимым.
#теперь попробуем запросить данные из БД и отобразим список статей на главной странице сайта. Для этого нужно импортировать модели из файла models из нашего приложения в файл views.py. Там пока только одна модель БД



# def categories(request):#эта функция для ссылки без нумерации
# 	return HttpResponse("<h1>Статьи по категориям</h1>")



# def categories(request, catid):#прописали параметр catid для переъхода по нумерации страниц
# 	# if (request.GET):#сделали проверку, на то что пустой запрос GET или нет
# 	# 	print(request.GET)#вывели словарь из параметров запроса. Сработает это когда мы обратимся к этому представлению. <QueryDict: {'name': ['Gagarina'], 'cat': ['music']}>. Без гет запроса словарь не будет выводиться
# 	# if (request.POST):#можно писать и пост запросы, о них будет речь идти далее
# 	# 	print(request.POST)
	# return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")#но без цифры страница не откроется, нужно именно с цифрой ссылку открывать. Также должно быть именно число, так как мы прописали тип int для catid. Типы которые можно указать перечислил в файле main.py

# def categories(request, cat):#это просто фунция для ссылки не с числами после cats и с буквами, тоже бывает надо прописать такую ссылку. 
# 	return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")

#функция categories с get запросом
# def categories(request, catid):
# 	if (request.GET):
# 		print(request.GET)#тут будет просто выведен словарь GET состоящий из ключей и значений (name=Gagarina и type=pop например). НА странице можно перейти по ссылке например такой: 127.0.0.1:8000/cats/music/?name=Gagarina&type=pop и словарь будет выведен в консоли. Если ссылку для GET запроса не писать то словарь будет пустым и он не выведется. Такую же проверку можно сделать и с POST запросом.
# 	return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")





# def changes(request, chang):#прописали параметр chang для переъхода по нумерации страниц с использованием типа slug, чтобы можно было писать строки вместо цифр
# 	return HttpResponse(f"<h2>Выборки по разделам</h2><p>{chang}</p>")

# def archive(request, year):#year потому что его определяли в регулярном выражении, по аналогии как с catid	
	
	# return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

# def archive(request, year):
# 	# if int(year) > 2023:#генерация ошибки с помощью класса Http404, его также нужно импортировать из django.http. Если ввести год больше чем 2023, то будет страница не найдена и сработает функция pageNotFound, которую мы написали ниже. Аналогично можно и сделать обработчики для других ошибок: handler500 - ошибка сервера, handler403 - доступ запрещен, handler400 - невозможно обработать запрос. ТО есть также сделать функцию в текущем файле views, сделать константу в urls.py в корневой папке проекта, и имортировать из django.http. Не забывает про константу DEBUG у нее должно быть значение False, если будет тру, то будет выводиться отладочная инфа, она нужна только разработчикам при отладке сайта. Также есть документация к этим обработчикам исключений
# 	# 	raise Http404()
#
# 	if int(year) > 2023:
# 		# return redirect('/', permanent=True)#функция redirect импортируется из модуля django.shortcuts. создали редирект, функцию redirect также нужно импортировать. Если просто слеш написать то мы вернемся на корневую страницу. Функция перекидывает нас в случае если мы напишем в ссылке год больше чем 2023. Редирект будет в этом случае с кодом 302. Без permanent=True будет редирект 302 то есть временный, с permanent=True будет постоянный 301. Эту функцию нужно обязательно возвращать return. Также не желательно прописывать явную страницу редиректа, так как она может измениться и потом будут ошибки
# 		# return redirect('/', permanent=False)
# 		return redirect('main', permanent=False)#прописали редирект на имя main, его также мы прописали в файле urls.py нашего приложения

	# return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


# def add_page(request):
# 	# form = AddPostForm()#создали объект на основе нашего класса формы.
# 	if request.method == 'POST':#когда первый раз заходим на страницу, то request.method принимает значение None, потому что мы не передавали никакие данные. и мы перейдем на else, то есть просто создаим объект с пустой формой. А если пользователь нажем вход, то метод будет не пустой и мы перейдем на другую ветку условия.
# 		form = AddPostForm(request.POST)#это форма с заполненными данными.
# 		if form.is_valid():#это проверка корректно ли были заполнены данные и переданы на сервер. Если проверка не пройдет, то джанго будет писать ошибку сам. НАпример проверку на русские буквы в поле slug.
# 			# print(form.cleaned_data)#если это так то в консоль выведутся очищенные данные.
# 			try:#тут напишем добавление записи в БД
# 				Home.objects.create(**form.cleaned_data)#создается объект в БД
# 				return redirect('main')#и переход на главную страницу
# 			except:
# 				form.add_error(None, 'Ошибка добавления поста')#иначе выводится ошибка если данные не валидны
# 	else:
# 		form = AddPostForm()

# 	return render(request, 'home/addpage.html', {"form": form , 'menu': menu, 'title': 'Добавление статьи'})#пока только прописали редирект на другую страницу addpage.html. Теперь при переходе по ссылке Добавление статьи будет открываться другая страница

#в джанго есть специальный класс Form, на базе которого можно делать классы форм. Все классы форм прописывают обычно в отдельном файле forms.py, который находится в папке с приложением. Создадим этот файл и перейдем в него
#при заполнении формы пользователь после того как заполнил, отправляет их на сервер, чтобы они записались в БД, при отправке эти данные проверяются на корректность, если что то не так, то сайт возвращается на ту же страницу где был пользователь и там в полях формы должны быть те же данные которые пользователья заполнил до этого. Если все хорошо, то мы переходим на какую-то другую страницу. Как это реализовать описал выше. Далее перейдем в файл forms.py для того чтобы прописать поля формы русскими буквами, для этого есть параметр label у каждого поля


#перепишем функцию add_page
# def add_page(request):
# 	if request.method == 'POST':
# 		form = AddPostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()#сохранили данные в БД. Этот метод save также сам генерирует сообщения об ошибках. и тут трай экспет не нужен уже.
# 			return redirect('main')#и переход на главную страницу
# 	else:
# 		form = AddPostForm()
#
# 	return render(request, 'home/addpage.html', {"form": form , 'menu': menu, 'title': 'Добавление статьи'})

#далее разберемся с полем фото. Идем в файл forms.py и допишем туда в список photo. Также в функции add_page при создании объекта AddPostForm добавим параметр request.FILES. И в шаблоне addpage.html допишем enctype="multipart/form-data" в строке когда мы объявляли форму в первом теге form, его атрибут нужно указывать когда передаем в форму какие либо файлы. Также путь к файлу джанго сам прописывает. 

#Валидация. В модели описываем свойства полей. Они нужны потом для валидации. Для sqlite длина поля обрезается сама по себе, в других СУБД длина поля будет срабатывать. В джанго также можно сделать и свой собственный валидатор. Как это работает. После введения данных от пользователя данные отправляются на сервер и сначала проходит валидация стандартная от функции save() потом от нашей функции is_valid() которую мы сами напишем. Чтобы сделать собственный валидатор перейдем в файл forms.py. В классе AddPostForm нужно написать функцию с названием clean_+название поля. Называть нужно именно так. Перейдем в файл forms.py

#пропишем класс CreateView вместо функции addpage

class AddPage(CreateView):
	form_class = AddPostForm#тут указываем ссылку на класс формы, который теперь будет связан с классом представления AddPage. Класс CreateView работает именно с формами.
	template_name = 'home/addpage.html'#тут просто указали шаблон формы.
	#далее такжде пропишем в urls.py ссылку на класс AddPage.as_view()
	success_url = reverse_lazy('main')

	def get_context_data(self, *, object_list=None, **kwargs):#добавим также функцию для отображения верхнего меню
		context = super().get_context_data(**kwargs)
		context['title'] = 'Добавление статьи'
		context['menu'] = menu
		return context
	#при добавлении сразу перейдем к новому посту. Это происходит потому что джанго использует get_absolute_url автоматом. В случае если нет такого метода у модели, то можно указать атрибут success_url = reverse_lazy('название маршрута') и ему нужно присвоить адрес маршрута на который мы будем перенаправляться после добавления статьи. reverse_lazy Нужно также импортировать. Используем эту функцию reverse_lazy а не reverse, потому что она формирует маршрут только когда он понадобится. Ее даже лучше использовать она более безопасная.







def contact(request):
	return HttpResponse("Обратная связь")


def login(request):
	return HttpResponse("Авторизация")


# def show_post(request, post_slug):
# 	post = get_object_or_404(Home, slug=post_slug)#эта функция ищет в БД запись с нужным нам параметром pk, который мы передаем в функцию. Если он не найдется то будет ошибка 404. Эту функцию get_object_or_404 также нужно импортировать из django.shortcuts
#
# 	context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,#post это объект класса Home со свойствами, и у него есть свойство cat_id. Из-за этого параметра шаблон знает какую группу сделать выбранной
#     }#это словарь из параметров, которые будем передавать шаблону post.html. Далее сделаем шаблон post.html.
#
# 	return render(request, 'home/post.html', context=context)

#теперь сделаем отображение статей по слагу, идем в файл models.py и добавляем туда поле слаг в БД. Удалим миграции чтобы заново сформировать БД. сам файл БД тоже надо удалить при добавлении новых полей. И также в поле cat уберем параметр Null. И после создания БД надо также создать суперпользователя. ВОбщем слаг это строка в адресной строке и ее пишем в БД, то есть часть ссылки на страницу записывается в БД. Также чтобы поле слаг, ссылка то есть, заполнялась автоматом в админке джанго на основании имени при добавлении поля, можно в файле admin.py указать строку prepopulated_fields = {"slug": ("name", )} в классе CategoryAdmin. Также можно и корректировать урл-ку.
#для таблицы home также сделаем такую штуку для автозаполнения урлки из админки prepopulated_fields = {"slug": ("title",)}. Далее заполним бд через админку. Потом также нужно сделать так чтобы в строке ссылки отображался слаг вместо цифры, чтобы слаг подтягивался из БД. Идем в файл urls.py в папке с приложением. Тип данных в post нужно поставить slug вместо int, и название переменной поменяем на post_slug. Также в функции show_post нужно заменить название переменных. И фильтр тоже сделаем по полю slug. Также в файле моделей нужно изменить get_absolute_url, также слаги прописать. Переделать по слагу и категории, у меня пока не получилось.


class ShowPost(DetailView):#сделали клас вместо функции show_post, он нужен для открытия поста, похож на ListView. Далее пропишем в urls.py назвнаие функции класса. Там помимо название функции нужно еще изменить и название слага, но наше название которое мы там укажем можно прописать и в классе. По умолчанию берется название по названию поля slug.
	model = Home
	template_name = 'home/post.html'
	slug_url_kwarg = 'post_slug'#указали название слага
	# pk_url_kwarg это для указния идентификатора pk вместо слага
	context_object_name = 'post'#это чтобы в шаблон передавался нужный нам элемент с данными таблицы.
	#также при указании несуществующего слага, также отобразится страница 404
	def get_context_data(self, *, object_list=None, **kwargs):#также передадим функцию для вывода меню сверху
		context = super().get_context_data(**kwargs)
		context['title'] = context['post']
		context['menu'] = menu
		return context
	#далее сделаем еще класс для добавления статьи CreateView вместо функции addpage. И конечно все такие классы нужно импортировать.





# def show_category(request, cat_slug):
# 	# cat = get_object_or_404(Home, slug=cat_slug)
# 	# posts = Home.objects.filter(slug=cat_slug)  # фильтруем по cat_id которые передаем в запросе
# 	# # cats = Category.objects.all()
# 	cat = Category.objects.filter(slug=cat_slug)
# 	posts = Home.objects.filter(cat_id=cat[0].id)  # фильтруем по cat_id которые передаем в запросе
#
# 	if len(posts) == 0:#это нужно, чтобы в случае когда нет постов, то была бы ошибка 404
# 		raise Http404()
#
# 	context = {
# 		"posts": posts,
# 		# 'cats': cats,
# 		"menu": menu,
# 		'title': 'Отображение по рубрикам',
# 		'cat_selected': cat[0].id, #далее модифицируем функцию show_categories, чтобы отображать статьи по отдельным рубрикам.
# 	}
# 	return render(request, "home/index.html", context=context)
# 	# return HttpResponse(f"Отображение категории с номером = {cat_id}")

class HomeCategory(ListView):
	model = Home
	template_name = 'home/index.html'
	context_object_name = 'posts'
	allow_empty = False

	def get_queryset(self):
		return Home.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)#выбираем только те категории которые соответствуют указанному слагу.
	#через переменную kwargs можно получать все параметры маршрута, то есть это словарь и по ключам можно обращаться к переменным. Тут будут выбраны все записи у которых слаг совпадает со слагом категории. То есть выбранная категория совпадает с категорией записи из таблицы. И еще статья должна быть опубликована.
	# У модели Home есть параметр cat который ссылается на модель категорий, cat__slug это означает что мы обращаемся к полю slug таблицы категорий. Такж в urls.py нужно прописать название метода HomeCategory.as_view()

	def get_context_data(self, *, object_list=None, **kwargs):#сделали функцию для того чтобы отображалась панель сверху
		context = super().get_context_data(**kwargs)
		context['title'] = 'Категория - ' + str(context['posts'][0].cat)#тут мы берем отфильтрованный список с одной категорией, который берется из словаря по ключу posts, и чтобы обратиться к объекту мы берем нулевой индекс, потом берем свойство объекта cat и его делаем строкой. Потом добавляем к ней строку 'Категория - ' и эт о все записывается в переменную title.
		context['menu'] = menu
		context['cat_selected'] = context['posts'][0].cat_id#сздесь берем идентификатор, а не категорию. Есть нюанс, когда мы напишем несуществующий слаг, то будет ошибка list index out of range. Но можно сдедать так чтобы генерировалась ошибка 404 страница не найдена. Для этого нужно прописать выше атрибут allow_empty = False. В случае если он равен False, тогда ошибок возникать не будет. У нас тут возникло дублирование кода, но это можно исправить с помощью миксинов, то есть сделать базовый класс для наших представлений и с него наследоваться.
		return context
		# далее сделаем класс DetailView для отображения конкретной страницы, в нашем случае для отображения страницы постов. заменим функцию show_post





def pageNotFound(request, exception):#эта функция для обработки исключения pageNotFound. И также в файле settings в папке нашего проекта (не приложения) нужно в константе DEBUG указанть значени False, тогда будет выводиться просто надпись, а не служебная инфа с ошибкой 404. Также нужно указать в этом файле разрешенные хосты в константе ALLOWED_HOSTS, то есть нужно прописаь IP адрес хоста, в нашем случае это localhost или 127.0.0.1 в кавычках. Без этой функции будет по анг писать Not Found. Также нужно в файле urls или проекта или приложения в переменную handler404 записать название функции которая будет отвечать за страницу в момент когда она не может отобразиться. Также можно генерировать исключение и вызывать эту функцию, тогда при срабатывании исключения будет выводиться наша страница
	return HttpResponseNotFound('<h1>Нет такой страницы</h1>')#HttpResponseNotFound нужно также импортировать










