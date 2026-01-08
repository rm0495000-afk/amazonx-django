import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

if os.environ.get("RENDER"):
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
    except Exception as e:
        pass