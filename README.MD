# portfolio-admin

Django admin dashboard and API for portfolio website. API Docs available under `/docs/`.

## Running
- run migrations
- set environment variables
- `python manage.py runserver`

## Environment variables
| NAME              | TYPE   | REQUIRED | DEFAULT |
|-------------------|--------|----------|---------|
| SECRET_KEY        | string | X        | N/A     |
| DEBUG             | bool   |          | false   |
| ALLOWED_HOSTS     | list   | X        | N/A     |
| DB_ENGINE         | string | X        | N/A     |
| DB_OPTION_DRIVER  | string | X        | N/A     |
| DB_NAME           | string | X        | N/A     |
| DB_USER           | string |          | N/A     |
| DB_PASSWORD       | string |          | N/A     |
| DB_PORT           | number |          | N/A     |
| DB_HOST           | string |          | N/A     |
| CORS_WHITELIST    | list   |          | []      |