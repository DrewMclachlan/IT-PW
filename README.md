# IT-PW
Pull the repo
Once installed dependencies must be installed on local machine. 
Using 'pip install' on the following in the root dir of the folder 'participants_wanted'

Django==2.1.5

django-crispy-forms==1.9.0

Pillow==5.4.1

pytz==2019.3

this can also be viewed local by running pip freeze > requirements.txt in the terminal
once done next step is to make database migrations and populate db in the terminal: 

python manage.py makemigrations
python manage.py migrate
python population_script.py

Then run the server with:
python manage.py runserver
