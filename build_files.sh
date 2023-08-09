echo "BUILD START"
python -m pip install requirements.txt
python manage.py collectstatic --noinput --clear
echo "BUILD END"