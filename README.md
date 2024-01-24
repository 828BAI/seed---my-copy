# seedstartups

Step by Step Guide:

Important: you need to have a database in postgresql named seed running on port 5433


Backend

    Cd backend
    Install virtual environment
    Launch virtual environment
    pip install -r requirements.txt
    cd src
    python manage.py makemigrations accounts
    python manage.py makemigrations projects
    python manage.py makemigrations meetings
    python manage.py migrate
    python manage.py runserver 8080



Node:

    cd frontend
    node index.js


Front-end:

    cd frontend
    cd seed-front
    npm start


