# enCuba Backend (Django)

A simple Django-based API for managing geographically located places and their reviews. This project allows you to add places with geographical coordinates, create reviews for those places, and filter them based on various criteria.

## ⚠️ Project Status
This project is currently **discontinued**. It's being made available as a reference implementation that others might find useful for similar needs.

## Features

- Add places with geographical coordinates (latitude/longitude)
- Create and manage reviews for places
- Filter places by:
  - Location (proximity to coordinates)
  - Category
  - Other relevant criteria

## Getting Started

### Prerequisites
- Python 3.8+
- Django 4.0+
- Django REST Framework
- PostgreSQL with PostGIS (recommended for spatial queries)
- (Additional dependencies will be listed in requirements.txt)

### Installation

1. Clone the repository
```bash
git clone [repository-url]
cd geo-places-api
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Create a `.env` file based on `.env.example` and update the values as needed.

5. Run migrations
```bash
python manage.py migrate
```

### Running the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Documentation

API endpoints are documented using Django REST Framework's built-in web interface. After starting the development server, you can access:

- Browsable API: `http://127.0.0.1:8000/api/schema/swagger-ui/`
- Admin interface: `http://127.0.0.1:8000/admin/` (requires superuser account)

