from django.apps import AppConfig

#это класс применяется для конфигурации всего приложения home
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
    verbose_name = "Самые крутые дома всего мира"#это название приложения в админке. Также можно его использовать в разных модулях джанго
