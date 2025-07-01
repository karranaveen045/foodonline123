# create_admin.py
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin02@gmail.com", "admin123")
    print("✅ Superuser created.")
else:
    print("⚠️ Superuser already exists.")
