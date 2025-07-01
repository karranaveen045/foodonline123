import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodonline.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="rohit123").exists():
    User.objects.create_superuser(
        username="rohit123",
        email="rohit123@example.com",
        password="admin123",
        first_name="Rohit",
        last_name="Kumar"
    )
    print("✅ Superuser created.")
else:
    print("⚠️ Superuser already exists.")
