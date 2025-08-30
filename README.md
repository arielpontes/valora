# Valora

Django Property Estimate Tool with AI integration.

## Setup instructions

Start the app using docker compose:

```bash
docker compose up -d
```

Exec into the web service container:

```bash
docker compose exec web bash
```

There you can run the migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

And start the development server:

```bash
python manage.py runserver 0:8000
```

The application will be available at http://localhost:8000.

## Testing

Inside the web service container, just run:

```bash
pytest
```
