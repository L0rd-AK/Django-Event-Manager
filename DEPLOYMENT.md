# Django Event Management System

A comprehensive event management system built with Django that allows users to manage events, categories, and participants.

## Features

- Event management with CRUD operations
- Category organization
- Participant registration and management
- Dashboard with statistics
- Search and filtering functionality
- Responsive design
- Admin interface

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create sample data (optional):
   ```bash
   python manage.py create_sample_data
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment on Render

This project is configured for easy deployment on Render.

### Automatic Deployment

1. Connect your GitHub repository to Render
2. Create a new Web Service
3. Use the following settings:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn event_management.wsgi:application`
   - **Environment Variables**:
     - `DEBUG`: `False`
     - `SECRET_KEY`: (Generate a new secret key)

### Manual Deployment Steps

If automatic deployment doesn't work, follow these steps:

1. Make sure your `build.sh` is executable:
   ```bash
   chmod +x build.sh
   ```

2. The build script will:
   - Install dependencies
   - Collect static files
   - Run database migrations
   - Create sample data

### Environment Variables

Set these environment variables in your Render dashboard:

- `DEBUG`: Set to `False` for production
- `SECRET_KEY`: Generate a new Django secret key for production

### Troubleshooting Deployment

If you get database errors:

1. Make sure migrations are applied:
   ```bash
   python manage.py migrate
   ```

2. Check if tables exist:
   ```bash
   python manage.py dbshell
   .tables  # for SQLite
   ```

3. If needed, reset migrations (WARNING: This will delete data):
   ```bash
   python manage.py migrate events zero
   python manage.py migrate
   ```

## Project Structure

```
event_management/
├── event_management/       # Main project directory
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── events/               # Events app
│   ├── models.py         # Database models
│   ├── views.py          # Views
│   ├── forms.py          # Forms
│   ├── urls.py           # App URL configuration
│   └── management/       # Custom management commands
├── templates/            # HTML templates
├── static/              # Static files
├── requirements.txt     # Python dependencies
├── build.sh            # Render build script
└── render.yaml         # Render configuration
```

## Models

- **Category**: Event categories with name and description
- **Event**: Events with name, description, date, time, location, and category
- **Participant**: Participants with name, email, and many-to-many relationship with events

## Key Features Implemented

1. **CRUD Operations**: Complete Create, Read, Update, Delete for all models
2. **Search and Filtering**: Event search by name and location with date range filters
3. **Database Optimization**: Uses select_related and prefetch_related for query optimization
4. **Dashboard**: Statistics and overview of events and participants
5. **Responsive Design**: Mobile-friendly interface
6. **Admin Interface**: Django admin for data management
7. **Production Ready**: Configured for deployment with proper security settings

## Development Notes

- Debug toolbar is only enabled in development mode
- Static files are served using WhiteNoise in production
- Database migrations are automatically run during deployment
- Sample data can be created using the custom management command
