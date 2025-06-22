set -o errexit

python manage.py migrate

#poetry install

#pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate