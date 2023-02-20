rm -rf hangrymealsapi/migrations
rm db.sqlite3
python3 manage.py migrate
python3 manage.py makemigrations hangrymealsapi
python3 manage.py migrate hangrymealsapi
python manage.py loaddata user
python manage.py loaddata ingredient
python manage.py loaddata recipe
python manage.py loaddata recipeingredients
python manage.py loaddata week
python manage.py loaddata pantry
python manage.py loaddata pantryingredient
