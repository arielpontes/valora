# Valora

Django Property Estimate Tool with AI integration.

## Development

To start the development server, first start the app:

```bash
docker compose up
```

You can then go into the web service:

```bash
docker compose exec web bash
```

And run the development server:

```bash
python manage.py runserver 0:8000
```

The application will be available at http://localhost:8000.

## Testing

Inside the web service, just run:

```bash
pytest
```
