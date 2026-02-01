# URL Shortener (Django)

A URL shortener web application built with Django that supports:
- User registration/login/logout
- Create short URLs (Base62)
- Manage URLs (list/edit/delete)
- Click analytics (count)
- Optional: Custom aliases, Expiration time, QR code generation

---

## Features

### Authentication
- Users can register, log in, and log out.
- Only authenticated users can create/manage short URLs.

### URL Shortening
- Users enter a long URL and receive a short URL.
- Short key generation uses Base62 encoding (derived from DB id).
- Visiting a short URL redirects to the original URL.

### URL Management
- Users can view all their created short URLs.
- Users can edit or delete their short URLs.
- Shows creation date + click count.

### Basic Analytics
- Each short URL tracks number of clicks.

### Bonus (Optional)
- Custom short URLs (alias)
- Expiration time
- QR code generation (`GET /qr/<code>/` returns PNG)

---

## Tech Stack
- Python
- Django
- SQLite (default, for development)

---

## Setup Instructions

### 1) Clone the repo
```bash
git clone https://github.com/Rohan-Dh/Url-Shortener.git
cd Url-Shortener
virtualenv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver