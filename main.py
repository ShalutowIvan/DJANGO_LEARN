# посмотреть дударя уроки по джанго, там вроде тоже норм
#1. Django - что это такое, порядок установки | Django уроки!!!!!!!!!!!!!!!!!
# Установка джанго
# устанавливаем виртуальное окружение
# python -m venv venv
#второй venv это имя виртуального окружения. В него будут ставиться все модули
# активируем его, для винды:
# .\venv\Scripts\activate
# После активации мы как бы войдем в виртуальное окружение и далее все установки будут в это виртальное окружение
# Для линукс активация
# source venv/bin/activate
# чтобы выйти из виртуального окружения пишем:
# deactivate
#после этого все модули будут тянуться из глобального окружения компа
# в пайчарме тоже можно указать виртуальное окружение. Через файл сеттингс
# с помощью ядра можно создавать сайты в рамках текущего окружения
# команда для список команд ядра:
# django-admin
# команда создания проекта первого сайта:
# django-admin startproject <имя сайта>
# имя сайта обычно совпадает с именем домена на котором располагается сайт. Сайт это как бы проект, в котором будет несколько приложений джанго.
# будет создана папка с именем которое мы напишем, в ней будет еще одна папка с таким же названием, это вложенная папка это пакет конфигурации сайта. В ней есть несколько файлов с конфигурациями, это пакет конфигурации с файлом __init__.py, то есть пакетная папка
# также в корне папки будет файл manage.py через него производится управление сайтом. ПО факту это утилита которая передает команды в django-admin и выполняет их от лица нашего сайта
# команда для запуска сервера из консоли из папки с имененем сайта:
# python manage.py runserver
#виртуальное окружение должно быть активировано
# чтобы остановить сервер нужно нажать CTRL+C
# он автоматом перезапускается когда что то редактируем в коде проекта. Но если изменения не происходят, то можно руками перезапустить вебсервер, то есть выключить и включить
#также при первом запуске у нас появится файл базы данных sqlite3. Эту СУБД джанго использует по умолчанию. Но можно подключать и другие
# также можно для запуска указывать свой порт. для этого пишем команду в консоли:
# python manage.py runserver <номер порта>
# или можно указать IP, тогда будет указан другой IP не стандартный. На локальном пк может не сработать
# python manage.py runserver IP:port

#2. Модель MTV. Маршрутизация. Функции представления | Django уроки!!!!!!!!!
# запрос пользователя -> маршрутизация по URL то есть ссылка -> ищет совпадение адреса -> активируется представление запроса, если ни один из шаблонов(шаблон это ссылка на страницу сайта, представление это вобщем отображение сайта) не совпадает то генерируется ошибка 404 (хотя мне кажется поиск гугл откроется) -> 
# как работает представление: берет некий шаблон то есть сам html шаблон (Templates), наполняет страницу данными из БД это модель данных(models), данные из БД это называется моделью. Далее результат отдается пользователю(views). То есть html наполненная данными из БД отображается пользователю в виде представления страницы.
# Такая модель называется MTV - model templates views это такой паттерн. Джанго использует этот паттерн MTV. Тут можно все функции делать отдельно
# структура сайта
# Сайт:
# Основное приложение
# Форум
# Опросник
# .....
# каждая часть сайта это отдельное приложение, они должны быть не зависимы друг от друга, чтобы можно было использовать в другом проекте
# создание приложения через консоль
# python manage.py startapp <имя приложения>
# будет создана папка с файлами в виде пакета в проекте. То есть каждое приложение в джанго это пакет
# состав пакета:
# - папка migrations для хранения миграций БД приложения
# admin.py для связи с админ панелью сайта. Админ панель поставляется вместе с джанго и каждый сайт может ее использовать
# apps.py - небходим для настройки и конфигурации текущего приложения
# models.py для хранения ОРМ моделей, для представления данных из Бд
# test.py это модуль с тестирующими процедурами
# views.py для хранения представлений или контроллеров текущего приложения. По сути как бы ссылки сайта нашего.
# приложение создали. Далее нужно зарегистрировать его в проекте нашего сайта, чтобы фреймворк джанго знал о его существовании. Для этого нужно войти в settings.py в папке с проектом
# регистрация приложения в джанго !!!
# заходим в файл settings.py в папке с проектом
# в файле ищем список INSTALLED_APPS. В нем прописаны все приложения, которые инсталированы в нашем пакете. В этот список нужно дописат название нашего приложения, то есть название файла без расширения в кавычках
# по факту джанго после добавления нашего приложения при запуске обращается к файлу apps.py и обращается к классу HomeConfig. Название класса состоит из названия приложения и слова Config. Поэтому в список в файле settings.py лучше добавить полный путь классу (в нашем случае это home.apps.HomeConfig).
# Сделаем обработчик главной страницы сайта. Нужно сделать представление - views. Они могут быть или в виде функций или в виде файлов
# Все представления находятся в файле views.py в папке с нашим приложением то есть в пакете приложения. Там прописываются классы и функции. Продолжение в этом файле....

# в папке с проектом пишется в файле urls.py ссылка на домашнюю страницу сайта, то есть стартовую, а в файле urls.py из папки с приложением пишутся маршруты для приложений

# типы данных в джанго для УРЛ
# str - любая не пустая строка, исключая символ "/"
# int - любое положительное число включая 0
# slug - слаг, то есть латиница ASCII таблицы символы дефиса и подчеркивания
# uuid - цифры, малые латинские символы ASCII, дефис
# path - любая не пустая строка включая символ "/"
# остановился на 5 мин, видео 3
# еще можно использовать регулярные выражения для указания path для url. Функция называется re_path()

# Маршрутизация, обработка исключений запросов, перенаправления | Django уроки!!!!!!!!!!!!!!!!
# структура урл адреса может содержать параметры:
# ?имя параметра то есть ключ=значение&ключ=значение и тд
# до записи выше также может идти префикс, и потом пары ключей и значений
# например:
# http://127.0.0.1:8000/?name=Gagarina&cat=music
# это пример GET запроса
# обратиться к параметрам GET запроса можно через request.GET это специальный словарь в котором сохраняются все эти данные
# исключения при входе на несуществую страницу можно посмотреть в файле settings.py. Далее там записи

# есть еще редиректы 
# 301 - страница перемещена на другой постоянный URL-адрес
# 302 - страница перемещена временно другой URL-адрес
# редиректы нужно писать тоже в представления views







