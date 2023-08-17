from django.db import models
from django.urls import reverse


# Create your models here.
class Home(models.Model):#название класса придумываем сами. Название класса это название таблицы. Также класс таблицы мы наследуем от базового класса Model, в нем есть необходимый функцинал для создания своих классов моделей таблиц. Также нужно иметь ввиду что поле id в базовом классе прописано по умолчанию и в классе его писать не нужно
	title = models.CharField(max_length=255, verbose_name="Заголовок")#это текствое поле и тип CharField с длинной 255. Описание типов полей есть в документации джанго http://djbook.ru/
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")#добавили поле слаг
	content = models.TextField(blank=True, verbose_name="Текст статьи")#это текстовое поле с расширенным диапазоном. blank=True означает что поле может быть пустым или False знаит не пустым
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")#это ссылка на фото. Фото будет загружаться в папку photos затем в подкаталоги год месяц день каждое фото в определенный подкаталог. Для этого параметра нужна еще дополнительная настройка. Для загрузки изображений и указания пути нужно настрить 2 константы MEDIA_ROOT = os.path.join(BASE_DIR, 'media'), MEDIA_URL = '/media/' и там нужно также импортировать os. Вообще мы испольщзуем отладочный сервер, и для загрузки файлов нужно сэмулировать реальный сервер для загрузки файлов. Для этого нужно зайти в urls.py в корневой папке проекта (не приложения), и там 
	time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")#Время создания статьи, тут будет приниматься время в момент добавления новой записи и не будет меняться в случае если указали auto_now_add=True. То есть это поле с указанием время создлания статьи
	time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")#время последнего редактирования. Это поле будет меняться каждый раз когда мы что-то меняем в текущей записи
	is_published = models.BooleanField(default=True, verbose_name="Публикация")#тут просто по умолчанию значение True
	cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категории")#указали поле cat, в название этого поля потом автоматом допишется cat_id самим джанго. Так как это поле это класс для свзи с другой БД. В классе прописали параметр Category - это первичная модель из которой тянется инфа по категории, в нашем случае она в виде строки, так как класс Category прописане после класса Home, если был бы до класса Home то можно было просто прописать без кавычек, получается можно писать и в кавычках и без. И укажем on_delete=models.PROTECT это для указания запрета удаления если есть ссылка на модель категории



	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post', kwargs={'post_slug': self.slug})#сделали формирование ссылки по идентификатору

	class Meta:#прописали внутренний мета класс для указания названия приложения в админке
		verbose_name = "Крутые дома"
		verbose_name_plural = "Крутые дома"#это для множественного числа, чтобы буква s не дописывалась автоматом
		# ordering = ['-time_create', 'title']#это нужно для сортировки записей в админке. сортировка идет по этим полям поочередно. Если поставить минус перед полем в списке, то будет обратная сортировка. Также эта сортировка прменяется не только к админке но и к выбранным записям модели Home на самом сайте. Также название самого приложения в админке можно изменить. Идем в файл apps.py



#мы все описали, теперь для создания БД нужно сделать механизм для миграций БД. Миграции - это наборы команд которые написаны на уровне ORM интерфейса. При создании миграции создаются новые или изменяются старые прежние таблицы и связи между ними. Каждый файл миграции помещается в папку migrations. На основе файлов миграции создается структура таблиц в БД. Файл миграции описывает изменения с таблицах, которые произошли в БД. Получается что-то похожее на контроллер версий, как будто гит. Поэтому мы можем откатиться в прежней версии БД. С помощью миграций можно изменять структуру таблиц. Но структуру лучше продумать заранее. 
#создание миграций, команда, ее нужно прописать в консоли:
#python manage.py makemigrations
#после выполнения этой команды в папке migrations должен появиться файл 0001_initial.py
#команда для создания sql запроса для создания таблицы:
#python manage.py sqlmigrate home 0001
# после выполнеия этой команды в консоли будет этот код:
# BEGIN;
# --
# -- Create model Home
# --
# CREATE TABLE "home_home" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(255) NOT NULL, "content" text NOT NULL, "photo" varchar(100) NOT NULL, "time_create" datetime NOT NULL, "time_update" datetime NOT NULL, "is_published" bool NOT NULL);
# COMMIT;
# home_home - это название приложения и название модели Бд, далее идут поля
#далее напишем команду для выполнения миграции также в консоли:
#python manage.py migrate
# если все удачно, то будет следующий текст:
# Operations to perform:
#   Apply all migrations: admin, auth, contenttypes, home, sessions
# Running migrations:
#   Applying contenttypes.0001_initial... OK
#   Applying auth.0001_initial... OK
#   Applying admin.0001_initial... OK
#   Applying admin.0002_logentry_remove_auto_add... OK
#   Applying admin.0003_logentry_add_action_flag_choices... OK
#   Applying contenttypes.0002_remove_content_type_name... OK
#   Applying auth.0002_alter_permission_name_max_length... OK
#   Applying auth.0003_alter_user_email_max_length... OK
#   Applying auth.0004_alter_user_username_opts... OK
#   Applying auth.0005_alter_user_last_login_null... OK
#   Applying auth.0006_require_contenttypes_0002... OK
#   Applying auth.0007_alter_validators_add_error_messages... OK
#   Applying auth.0008_alter_user_username_max_length... OK
#   Applying auth.0009_alter_user_last_name_max_length... OK
#   Applying auth.0010_alter_group_name_max_length... OK
#   Applying auth.0011_update_proxy_permissions... OK
#   Applying auth.0012_alter_user_first_name_max_length... OK
#   Applying home.0001_initial... OK
#   Applying sessions.0001_initial... OK

#то есть помимо нашей таблицы там есть вспомогательные таблицы по умолчанию от фреймворка джанго, и они автоматом создаются


class Category(models.Model):
	name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")#создали модель для таблицы с одним столбцом - категория. Также будет еще id, он создается автоматом. ПОле name будет индексировано db_index=True, и длинна будет 100
	slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
 
	def __str__(self):
		return self.name#возвращается имя категории
#далее в классе Home нужно прописать поле cat c ForeignKey

	def get_absolute_url(self):
		return reverse('category', kwargs={'cat_slug': self.slug})

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'#для множественного числа в названии
		ordering = ['id']#сортировка по ИД. Все метаописания вносятся в таблицу БД при миграциях
#при загрузке фото через админку джанго автоматом добавляет фото и создает папки по текущей дате и кидает туда фото. Далее можно в файлу index.html прописать наше фото


#потом попробуем сделать миграцию команда - python manage.py makemigrations. Но в нашем случае в таблице категории нет записей, и джанго при миграции задаст вопрос:
# Please select a fix:
#  1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
#  2) Quit and manually define a default value in models.py.
# Select an option: 2
#выберем пока 2
# УКажем в поле cat параметр , null=True, эо означает что оно может быть нулевым
#теперь миграции создадутся в папке makemigrations. Потом можно будет их выполнить команда - python manage.py migrate
#в дальнейшем так вносить миграции нельзя, так как нужно изначально продумать всю структуру таблиц, и потом только делать миграции, то есть создавать таблицы. Либо наверно можно удалить дб и создать таблицы заново. Добавим новые записи в таблицу категории.
# Для этого перейдем в терминал и там напишем - python manage.py shell - это для входа в оболочку фреймворка джанго
# имортируем модель - from home.models import *
#далее создадим там записи:
# Category.objects.create(name='Частные дома')
# Category.objects.create(name='Многоэтажки')
# В таблице category будут созданы 2 записи
# потом в таблице home выберем все записи
# w_list = Home.objects.all()
# и сделаем для них обновление через переменную w_list
# w_list.update(cat_id=1)
# в cmd выведется значение 3, это колво измененых записей.

# пояснения к таблице в джанго
# атрибуты title, content и тд это ссылки на объекты классов CharField, TextField и тд. Эти поля опредеяют набор и тип полей в БД, но не содержат данные записей из БД, и джанго через механизм миграции создает БД с нужными полями. Далее когда мы создаем объект класса Home и в нем есть параметры title, content и тд, вот они содержат инфу с какиим то значением то есть будет содержание. А свойство cat или cat_id это будет ссылка на объект класса Category. Это все поведение прописано в конструкторе базового класса, так как в классе Home нет конструктора, и поэтому он берется из родителя то есть из базового класса. То есть автоматом создаются локальные свойства с теми именами которые мы пропишем в модели БД. 
#если создать объект класса Home, то теперь title будет строкой. Раньше Home.title был объектом то есть просто в классе это объект, а теперь w1.title будет строкой тип str будет, то есть в когда создали объект то есть запись в бд, это уже строка. Тип данных у поля cat_id будет <class 'home.models.Category'>
#пока запись объектов не добавлена в БД, то там в полях которые формируются автоматом например w1.pk будет пусто то есть значения равны None.
# Если заново запустить консоль такими командами:
# >>> from home.models import *
# >>> w1 = Home(title="t1", content="c1", cat_id=1)
# >>> from django.db import connection
# >>> connection.queries
#то список sql запросов будет пустым
# теперь если вызвать w1.cat то будет прочитана 1 категория, то есть категория со значением id 1. Когда обращаемся к данным из БД джанго из делает SQL запрос с помощью кода питона.
# Создадим объект w2
# >>> w2 = Home.objects.get(pk=2)
# >>> connection.queries
#тут получается мы прочитали из бд запись и записали ее в переменную. 
# w2.cat
# {'sql': 'SELECT "home_category"."id", "home_category"."name" FROM "home_category" WHERE "home_category"."id" = 1 LIMIT 21', 'time': '0.000'}
#тут будет еще один sql запрос
#то есть при каждом чтении инфы из таблицы будет созда sql запрос из БД. 
# Атрибуты в классе модели БД это просто классы для создания БД, а сами объекты записи в БД это уже объекты с полями со значениями

# Далее перейдем в шаблон base.html и сделаем отображение списка категорий. Там они идут просто списком словами, мы сделаем чтобы из таблицы подтягивались

#также пропишем функцию get_absolute_url в классе Category. И маршрут пропишем в файле urls.py приложения home

# также в файле views.py нужно передать коллекцию cats в функции index

# добавим еще название категории и название поста


