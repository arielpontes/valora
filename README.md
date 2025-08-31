# Valora

Django Property Estimate Tool with AI integration.

## Setup instructions

First generate a `.env` file from the example:

```bash
cp .env.example .env
```

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

## Assumptions

User input will always be meaningful.

## Potential improvements with more time

Better data validation. Currently any inputs will generate a response. Ideally
sufficiently bad input should cause errors. The error messages in the front-end
should also be more user friendly instead of just alerts.
