# Healthcare Backend API

A RESTful healthcare backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication.

## Features

* User registration and JWT login
* Patient management
* Doctor management
* Patient-doctor mapping
* PostgreSQL database
* Authentication and authorization
* Input validation
* Database-level uniqueness constraints
* Django admin interface

## Tech Stack

* Python
* Django
* Django REST Framework
* PostgreSQL
* Simple JWT
* psycopg2
* python-dotenv

## API Endpoints

### Authentication

| Method | Endpoint              | Description                  |
| ------ | --------------------- | ---------------------------- |
| POST   | `/api/auth/register/` | Register a user              |
| POST   | `/api/auth/login/`    | Login and receive JWT tokens |

### Patients

| Method | Endpoint              | Description                 |
| ------ | --------------------- | --------------------------- |
| POST   | `/api/patients/`      | Create patient              |
| GET    | `/api/patients/`      | Get current user's patients |
| GET    | `/api/patients/<id>/` | Get patient details         |
| PUT    | `/api/patients/<id>/` | Update patient              |
| DELETE | `/api/patients/<id>/` | Delete patient              |

### Doctors

| Method | Endpoint             | Description        |
| ------ | -------------------- | ------------------ |
| POST   | `/api/doctors/`      | Create doctor      |
| GET    | `/api/doctors/`      | Get all doctors    |
| GET    | `/api/doctors/<id>/` | Get doctor details |
| PUT    | `/api/doctors/<id>/` | Update doctor      |
| DELETE | `/api/doctors/<id>/` | Delete doctor      |

### Patient-Doctor Mappings

| Method | Endpoint                      | Description                        |
| ------ | ----------------------------- | ---------------------------------- |
| POST   | `/api/mappings/`              | Assign doctor to patient           |
| GET    | `/api/mappings/`              | Get user's patient-doctor mappings |
| GET    | `/api/mappings/<patient_id>/` | Get doctors assigned to a patient  |
| DELETE | `/api/mappings/<id>/`         | Remove a mapping                   |

## Setup

Clone the repository and create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Create a PostgreSQL database and configure the following variables in `.env`:

```env
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432
```

Run migrations:

```bash
python manage.py migrate
```

Create an admin user:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

The API will be available at:

```text
http://127.0.0.1:8000/
```

## Authentication

Protected endpoints require a JWT access token:

```text
Authorization: Bearer <access_token>
```

## Security

* Passwords are hashed using Django's password hashing system.
* JWT authentication protects healthcare APIs.
* Patients are restricted to their creating user.
* Doctor modifications are restricted to the doctor creator.
* Patient-doctor mappings are restricted to the patient's owner.
* Duplicate patient-doctor assignments are prevented at the database level.
* Sensitive configuration is stored in environment variables.
