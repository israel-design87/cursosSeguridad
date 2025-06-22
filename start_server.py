import subprocess
import sys
import os

def run_command(command):
    print(f"Ejecutando: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"Error ejecutando: {command}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    # Puerto que Render asigna para la app
    port = os.environ.get("PORT", "10000")
    
    run_command("python manage.py migrate --no-input")
    run_command("python manage.py collectstatic --no-input")
    run_command(f"gunicorn cursosseguridad.wsgi --bind 0.0.0.0:{port}")