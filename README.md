
# Landmarks API

Wagtail CMS + API for Landmarks. 




## Deployment

Landmarks can be run via Docker or in a virtual environment as described below

### Run a Docker container:

Build

```bash
  docker build -t landmarks .
```

Run

```bash
  docker run --rm --name landmarks -p 8000:8000 -it landmarks
```

Create superuser

```bash
  docker exec -it landmarks python manage.py createsuperuser
```

### Run in virtual environment

Create a virtual environment named `venv` and activate it

```bash
  python3 -m venv venv && source venv/bin/activate
```

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