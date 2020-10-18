1. Go through Django tutorial
   https://docs.djangoproject.com/en/3.1/intro/tutorial01/

2. Create Virtual Env; Activate Virtual Env; pip instal -r requirements.txt

3. Install Mysql on your machine

4. Configure web app to use Mysql
   - cd mywebapp/mywebapp
   - Update settings.py DATABASES section

5. Apply migrations
   - cd ..
   - python manage.py migrate

6. Start web app
   - python manage.py runserver

7. Try following commands from another window (or browser):
   - curl http://127.0.0.1:8000/assignment3
   - curl http://127.0.0.1:8000/assignment3/libraries
   - curl -X http://127.0.0.1:8000/assignment3/libraries -d@library.json

8. Work on your assignment:
   - cd assignment3
   - Make changes to models.py
     - Reflect these changes into the tables:
       - cd ..
       - python manage.py makemigrations
       - python manage.py migrate
       - You will have to run 'makemigrations' and 'migrate' anytime you make any changes to models.py

   - Make changes to urls.py (if needed as per the assignment)
   - Make changes to views.py (if needed as per the assignment)
