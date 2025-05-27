from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    verbose_name = "Пользователи"


    def ready(self):
        from django.contrib.auth.models import Group
        group_names = ['customer','seller','staff_warehouse','staff_delivery']
        for name in group_names:
            Group.objects.get_or_create(name=name)
