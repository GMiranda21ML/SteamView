import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

django.setup()

from django.contrib.auth.models import User

User.objects.exclude(is_superuser=True).delete()

print("Todos os usuários, exceto o superusuário, foram deletados.")
