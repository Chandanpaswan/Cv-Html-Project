# Chandan Kumar Paswan CV Website

A database-backed professional CV and portfolio website built with Django, HTML, CSS, and JavaScript. The public site is rendered from Django models, and all profile content can be updated through Django Admin or the custom dashboard.

## Features

- Premium responsive public CV website
- Database-backed profile, about, experience, education, skills, services, projects, certifications, achievements, social links, contact messages, and SEO metadata
- Secure Django admin at `/admin/`
- Custom staff dashboard at `/dashboard/`
- Blog listing and SEO-friendly detail URLs at `/blog/`
- CSRF-protected contact form with database persistence
- Uploadable profile photo, project images, blog images, and CV PDF
- Dynamic title, description, canonical, Open Graph, Twitter, Schema.org, sitemap, and robots.txt support
- SQLite for development and `DATABASE_URL` PostgreSQL support for production
- WhiteNoise static file serving and secure production cookie/HTTPS settings

## Local setup

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py seed_cv
python manage.py createsuperuser
python manage.py runserver
```

Open `/`, `/blog/`, `/dashboard/`, `/admin/`, and `/sitemap.xml` on the local server. The `seed_cv` command creates Chandan's starter profile, experience, projects, skills, services, education, social links, SEO settings, and one published blog note. Upload the real profile photo and CV PDF from admin afterward.

## Content management

Sign in at `/admin/` or `/dashboard/` with a staff user. Edit Personal information for the name, title, contact details, WhatsApp, stats, profile photo, and CV PDF. Manage ordered public sections from their model menus; use `is_visible` to hide content and `sort_order` to control display order. Blog posts support publishing, categories, tags, slugs, featured images, and SEO metadata. Contact enquiries appear under Contact messages.

The public templates query only visible or published records, so admin changes appear automatically without editing HTML.

## Production

Set `DJANGO_DEBUG=0`, a long random `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, and a PostgreSQL `DATABASE_URL`. Then run:

```powershell
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py check --deploy
```

Run behind HTTPS with Gunicorn or Uvicorn. Store media on durable object storage or a persistent volume, configure email delivery for contact notifications, and never commit `.env`, `db.sqlite3`, or uploads.

## Project layout

```text
config/       Django settings and root URLs
cv/           CV models, public views, forms, admin, seed command
blog/         Blog model, public views, and admin
dashboard/    Staff-only overview dashboard
templates/    Public, blog, login, and dashboard templates
static/       CSS and JavaScript
media/        Local uploads (ignored by git)
```
