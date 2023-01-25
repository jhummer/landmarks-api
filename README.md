
# Landmarks API

Wagtail CMS + API for Landmarks. 




## Deployment


Install dependencies (preferably in a virtual environment)

```bash
  pip install -r requirements.txt
```

Setup the database

```bash
  python manage.py migrate
```

Create administrator
```bash
  python manage.py createsuperuser
```

Start webserver

```bash
  python manage.py runserver
```

## CMS

Log in to `http://localhost:8000/admin` and create some Landmark pages.

## API 

Browsable API can be found at `http://localhost:8000/api/pages/`. To filter only Landmark pages and include all fields use:

`http://localhost:8000/api/pages/?type=landmarks.LandmarkPage&fields=*`

## Have fun! 🚀