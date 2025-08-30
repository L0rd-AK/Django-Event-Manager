# Event Management System

A comprehensive Django-based event management system that allows users to manage events, categories, and participants with a modern, responsive interface built with Tailwind CSS.

## Features

### Core Functionality
- **Event Management**: Create, read, update, and delete events
- **Category Management**: Organize events into categories
- **Participant Management**: Register and manage event participants
- **Dashboard**: Overview of all events, categories, and participants
- **Search & Filter**: Find events by name, location, or category
- **Pagination**: Efficient browsing of large datasets

### Technical Features
- **Optimized Database Queries**: Uses select_related and prefetch_related
- **Responsive UI**: Mobile-first design with Tailwind CSS
- **Form Validation**: Client-side and server-side validation
- **Error Handling**: Proper error messages and user feedback
- **Admin Interface**: Django admin for backend management
- **CSRF Protection**: Security against cross-site request forgery

## Project Structure

```
event_management/
├── event_management/          # Main project directory
│   ├── __init__.py
│   ├── settings.py           # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── events/                   # Events app
│   ├── __init__.py
│   ├── models.py            # Category, Event, Participant models
│   ├── admin.py             # Admin configuration
│   ├── forms.py             # Django forms
│   ├── views.py             # View functions and classes
│   ├── urls.py              # App URL patterns
│   └── migrations/          # Database migrations
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   └── events/             # Event-specific templates
│       ├── dashboard.html
│       ├── event_list.html
│       ├── event_detail.html
│       ├── event_form.html
│       ├── event_confirm_delete.html
│       ├── category_list.html
│       ├── category_detail.html
│       ├── category_form.html
│       ├── category_confirm_delete.html
│       ├── participant_list.html
│       ├── participant_detail.html
│       ├── participant_form.html
│       └── participant_confirm_delete.html
├── static/                  # Static files (CSS, JS, images)
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

### Step 1: Clone or Download
```bash
# If using Git
git clone <repository-url>
cd event_management

# Or download and extract the ZIP file
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Database Setup
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
```

### Step 5: Run Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### Accessing the Application
- **Main Dashboard**: `http://127.0.0.1:8000/`
- **Admin Panel**: `http://127.0.0.1:8000/admin/`

### Main Features

#### Dashboard
- Overview of total events, categories, and participants
- Today's events display
- Quick navigation to all sections
- Interactive statistics

#### Event Management
- **List Events**: View all events with pagination and search
- **Create Event**: Add new events with category assignment
- **Event Details**: View event information and registered participants
- **Edit Event**: Update event information
- **Delete Event**: Remove events with confirmation

#### Category Management
- **List Categories**: View all categories with event counts
- **Create Category**: Add new event categories
- **Category Details**: View category information and associated events
- **Edit Category**: Update category information
- **Delete Category**: Remove categories with confirmation

#### Participant Management
- **List Participants**: View all participants with their registrations
- **Register Participant**: Add new participants and assign to events
- **Participant Details**: View participant information and event history
- **Edit Participant**: Update participant information
- **Remove Participant**: Delete participants with confirmation

### Search & Filtering
- **Event Search**: Search events by name or location
- **Category Filter**: Filter events by category
- **Date Filters**: View events by date range
- **Status Filters**: Filter by upcoming, ongoing, or past events

## Models

### Category
- `name`: Category name (unique)
- `description`: Category description
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Event
- `name`: Event name
- `description`: Event description
- `date`: Event date
- `time`: Event time
- `location`: Event location
- `category`: Foreign key to Category
- `created_at`: Creation timestamp
- `updated_at`: Last update timestamp

### Participant
- `name`: Participant name
- `email`: Email address (unique)
- `phone`: Phone number (optional)
- `events`: Many-to-many relationship with Event
- `created_at`: Registration timestamp
- `updated_at`: Last update timestamp

## API Endpoints

### Dashboard
- `GET /` - Dashboard view

### Events
- `GET /events/` - List all events
- `GET /events/create/` - Create new event form
- `POST /events/create/` - Create new event
- `GET /events/<id>/` - Event detail view
- `GET /events/<id>/edit/` - Edit event form
- `POST /events/<id>/edit/` - Update event
- `GET /events/<id>/delete/` - Delete confirmation
- `POST /events/<id>/delete/` - Delete event
- `GET /events/search/` - Search events

### Categories
- `GET /categories/` - List all categories
- `GET /categories/create/` - Create new category form
- `POST /categories/create/` - Create new category
- `GET /categories/<id>/` - Category detail view
- `GET /categories/<id>/edit/` - Edit category form
- `POST /categories/<id>/edit/` - Update category
- `GET /categories/<id>/delete/` - Delete confirmation
- `POST /categories/<id>/delete/` - Delete category

### Participants
- `GET /participants/` - List all participants
- `GET /participants/create/` - Register new participant form
- `POST /participants/create/` - Register new participant
- `GET /participants/<id>/` - Participant detail view
- `GET /participants/<id>/edit/` - Edit participant form
- `POST /participants/<id>/edit/` - Update participant
- `GET /participants/<id>/delete/` - Delete confirmation
- `POST /participants/<id>/delete/` - Delete participant

## Customization

### Styling
The application uses Tailwind CSS via CDN. To customize styles:
1. Modify the Tailwind classes in templates
2. Add custom CSS in `static/css/` directory
3. Update `base.html` to include custom stylesheets

### Adding New Features
1. Define new models in `events/models.py`
2. Create forms in `events/forms.py`
3. Add views in `events/views.py`
4. Define URL patterns in `events/urls.py`
5. Create templates in `templates/events/`

### Database Configuration
To use a different database (PostgreSQL, MySQL):
1. Install the appropriate database adapter
2. Update `DATABASES` setting in `settings.py`
3. Run migrations: `python manage.py migrate`

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (Production)
```bash
python manage.py collectstatic
```

### Debug Mode
The application runs in debug mode by default. For production:
1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS`
3. Set up proper static file serving
4. Configure production database

## Troubleshooting

### Common Issues

#### Python/Django Not Found
- Ensure Python is installed and in PATH
- Activate virtual environment if using one
- Install requirements: `pip install -r requirements.txt`

#### Database Errors
- Run migrations: `python manage.py migrate`
- Check database file permissions
- Reset database: Delete `db.sqlite3` and run migrations again

#### Template Not Found
- Check template paths in `settings.py`
- Ensure templates are in the correct directory structure
- Verify template names in views match file names

#### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` settings
- Ensure static files are in correct directories

### Getting Help
1. Check Django documentation: https://docs.djangoproject.com/
2. Review error messages in console
3. Check Django debug toolbar for performance issues
4. Verify database queries in admin panel

## License

This project is created for educational purposes as part of a Django assignment.

## Contributing

This is an assignment project. For educational use and reference only.
