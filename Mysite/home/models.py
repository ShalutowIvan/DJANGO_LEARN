from django.db import models

# Create your models here.
class Home(models.Model):#название класса придумываем сами. Название класса это название таблицы. Также класс таблицы мы наследуем от базового класса Model, в нем есть необходимый функцинал для создания своих классов моделей таблиц. Также нужно иметь ввиду что поле id в базовом классе прописано по умолчанию и в классе его писать не нужно
	title = models.CharField(max_length=255)#это текствое поле и тип CharField с длинной 255. Описание типов полей есть в документации джанго http://djbook.ru/
	content = models.TextField(blank=True)#это текстовое поле с расширенным диапазоном. blank=True означает что поле может быть пустым или False знаит не пустым
	photo = models.ImageField(upload_to="photos/%Y/%m/%d/")#это ссылка на фото. Фото будет загружаться в папку photos затем в подкаталоги год месяц день каждое фото в определенный подкаталог. Для этого параметра нужна еще дополнительная настройка. Для загрузки изображений и указания пути нужно настрить 2 константы MEDIA_ROOT = os.path.join(BASE_DIR, 'media'), MEDIA_URL = '/media/' и там нужно также импортировать os. Вообще мы испольщзуем отладочный сервер, и для загрузки файлов нужно сэмулировать реальный сервер для загрузки файлов. Для этого нужно зайти в urls.py в корневой папке проекта (не приложения), и там 
	time_create = models.DateTimeField(auto_now_add=True)#Время создания статьи, тут будет приниматься время в момент добавления новой записи и не будет меняться в случае если указали auto_now_add=True. То есть это поле с указанием время создлания статьи
	time_update = models.DateTimeField(auto_now=True)#время последнего редактирования. Это поле будет меняться каждый раз когда мы что-то меняем в текущей записи
	is_published = models.BooleanField(default=True)#тут просто по умолчанию значение True

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





