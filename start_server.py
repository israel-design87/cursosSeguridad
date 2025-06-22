import subprocess
import sys
import os


def create_superuser():
    from django.contrib.auth import get_user_model
    import django

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cursosseguridad.settings")
    django.setup()

    User = get_user_model()

    username = os.environ.get("DJANGO_SU_NAME")
    email = os.environ.get("DJANGO_SU_EMAIL")
    password = os.environ.get("DJANGO_SU_PASSWORD")

    if not (username and email and password):
        print("Variables de entorno para superusuario no definidas. Omitiendo creación.")
        return

    if not User.objects.filter(username=username).exists():
        print(f"Creando superusuario '{username}'...")
        User.objects.create_superuser(username, email, password)
    else:
        print(f"El superusuario '{username}' ya existe.")


def run_command(command):
    print(f"Ejecutando: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error ejecutando: {command}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    port = os.environ.get("PORT", "10000")

    run_command("python manage.py migrate --no-input")
    run_command("python manage.py collectstatic --no-input")

    create_superuser()

    run_command(f"gunicorn cursosseguridad.wsgi --bind 0.0.0.0:{port}")