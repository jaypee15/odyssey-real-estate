set -o errexit  # exit on error

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsu
postgres://odyssey_real_estate_user:SKTrGpBbeQkr6qPUiZQCDLZyJxF5b5vN@dpg-cmqa02i1hbls73ficao0-a/odyssey_real_estate