# Student Portal (Django)

A simple student login + dashboard.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py create_student   # creates STU001 / test1234
python manage.py createsuperuser  # optional, for /admin/
python manage.py runserver
```

Open http://127.0.0.1:8000/ and sign in with `STU001` / `test1234`.

## URLs

| URL            | Purpose                     |
|----------------|-----------------------------|
| `/`            | Student login               |
| `/dashboard/`  | Student dashboard           |
| `/logout/`     | Logout (POST only)          |
| `/admin/`      | Django admin                |

## Tests

```bash
python manage.py test
```

## Production notes

Set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` and `DJANGO_ALLOWED_HOSTS=example.com`
as environment variables before deploying.
