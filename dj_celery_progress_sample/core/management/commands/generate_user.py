from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Generating fake user by running python manage.py generate_user"

    def handle(self, *args, **kwargs):
        for i in range(0, 500):
            User.objects.create_user(
                username=f"username_{i}",
                password=f"password_{i}_123",
                email=f"username_{i}@email.com",
                first_name=f"first_name_{i}",
                last_name=f"last_name_{i}",
                is_superuser=i % 2 == 0,
                is_staff=i % 2 != 0,
            )
            print(f"Insrting item {i}")
