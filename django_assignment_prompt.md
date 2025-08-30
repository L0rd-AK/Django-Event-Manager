# Django Event Management System - Complete Assignment Prompt

## Assignment Overview
Create a fully functional Event Management System using Django that demonstrates ORM, optimized queries, and responsive design with Tailwind CSS. **Total: 100 Marks**

---

## SECTION 1: Data Models (15 Marks)

Create three Django models with the following exact specifications:

### 1.1 Category Model
```python
# Fields required:
- name (CharField, max_length=100)
- description (TextField)
```

### 1.2 Event Model
```python
# Fields required:
- name (CharField, max_length=200)
- description (TextField)
- date (DateField)
- time (TimeField)
- location (CharField, max_length=200)
- category (ForeignKey to Category model, on_delete=CASCADE)
```

### 1.3 Participant Model
```python
# Fields required:
- name (CharField, max_length=100)
- email (EmailField, unique=True)
- events (ManyToManyField to Event model, related_name='participants')
```

**Requirements:**
- Include proper `__str__` methods for all models
- Add appropriate `Meta` classes with ordering
- Ensure proper model relationships

---

## SECTION 2: CRUD Operations (10 Marks)

Implement full Create, Read, Update, Delete functionality for ALL models:

### 2.1 Event CRUD
- **Create**: Form to add new events with all fields
- **Read**: List view showing all events, Detail view for individual events
- **Update**: Edit form for existing events
- **Delete**: Delete functionality with confirmation

### 2.2 Participant CRUD
- **Create**: Form to add new participants
- **Read**: List view showing all participants, Detail view for individual participants
- **Update**: Edit form for existing participants
- **Delete**: Delete functionality with confirmation

### 2.3 Category CRUD
- **Create**: Form to add new categories
- **Read**: List view showing all categories, Detail view for individual categories
- **Update**: Edit form for existing categories
- **Delete**: Delete functionality with confirmation

### 2.4 Form Validation Requirements
- Implement proper Django forms with validation
- Prevent invalid data submission
- Show error messages for invalid inputs
- Include client-side and server-side validation

---

## SECTION 3: Optimized Queries (10 Marks)

Implement these specific query optimizations:

### 3.1 select_related Usage
- Use `select_related('category')` when listing events to fetch category data in a single query
- Example: `Event.objects.select_related('category').all()`

### 3.2 prefetch_related Usage
- Use `prefetch_related('participants')` when fetching events with their participants
- Example: `Event.objects.prefetch_related('participants').all()`

### 3.3 Aggregate Query
- Calculate total number of participants across ALL events
- Use Django's `Count` aggregation
- Display this count prominently in the dashboard

### 3.4 Filter Queries
Implement these specific filters:
- **Category Filter**: Filter events by their category
- **Date Range Filter**: Filter events between two specific dates
- Use proper QuerySet filtering methods

---

## SECTION 4: UI with Tailwind CSS (35 Marks)

### 4.1 Responsive and User-Friendly Interface (15 Marks)

#### Event Listing Page
- Display all events in a responsive grid/list
- Show for each event:
  - Event name and description
  - Date and time
  - Location
  - Category name
  - Participant count
- Make it responsive for mobile, tablet, and desktop

#### Event Detail Page
- Show complete event information
- Display ALL associated participants
- Include edit and delete buttons
- Show participant count and category details

#### Forms Interface
- Create responsive forms for adding/updating:
  - Events (with category dropdown)
  - Participants (with event selection)
  - Categories
- Include proper form styling with Tailwind CSS
- Add form validation styling (error states, success states)

### 4.2 Navigation and Styling (5 Marks)
- Create a consistent navigation bar with links to:
  - Dashboard
  - Events (List/Add)
  - Participants (List/Add)
  - Categories (List/Add)
- Ensure consistent styling across ALL pages
- Use Tailwind CSS for all styling (no custom CSS)

### 4.3 Organizer Dashboard (15 Marks)

Create a comprehensive dashboard with these EXACT components:

#### Stats Grid (Top Section)
Display four stat cards showing:
1. **Total Number of Participants** (aggregate count across all events)
2. **Total Number of Events**
3. **Number of Upcoming Events** (future date)
4. **Number of Past Events** (past date)

#### Today's Events Listing
- Below the stats grid, show events scheduled for TODAY
- Display event details in cards or list format

#### Interactive Stats Feature
Implement clickable stats that update content below:
- Clicking "Total Events" → Shows all events
- Clicking "Upcoming Events" → Shows only future events
- Clicking "Past Events" → Shows only past events
- Use AJAX or Django views to update content dynamically

---

## SECTION 5: Search Features (10 Marks)

### 5.1 Search Implementation
- Add search functionality to find events by:
  - Event name (case-insensitive)
  - Location (case-insensitive)

### 5.2 Technical Requirements
- Use `request.GET` to capture search text from URL parameters
- Use `icontains` lookup for case-insensitive searches
- Example query: `Event.objects.filter(name__icontains=search_term)`
- Add search form on events listing page
- Display search results with highlighting or indication

---

## TECHNICAL REQUIREMENTS

### Django Structure
- Follow Django's MVT (Model-View-Template) architecture
- Create proper URL patterns for all views
- Use class-based views where appropriate
- Implement proper error handling

### Tailwind CSS Requirements
- Use ONLY Tailwind CSS classes (no custom CSS)
- Ensure responsive design (mobile-first approach)
- Use Tailwind's component classes for consistency
- Implement proper color scheme and spacing

### Database & Queries
- Use Django ORM exclusively
- Implement the specified optimized queries
- Test query efficiency (mention Django Debug Toolbar usage)
- Ensure proper database relationships

### Additional Features
- Add proper pagination for large lists
- Include confirmation dialogs for delete operations
- Show success/error messages after operations
- Implement proper form handling with CSRF protection

---

## DELIVERABLES

Please provide:

1. **Complete Django Project Structure** with:
   - models.py (all three models)
   - views.py (all CRUD views + dashboard + search)
   - urls.py (all URL patterns)
   - forms.py (all Django forms)
   - All HTML templates with Tailwind CSS

2. **Key Files to Include:**
   - settings.py (with Tailwind CSS setup)
   - admin.py (register all models)
   - Migration files for models
   - Requirements.txt

3. **Specific Views Required:**
   - Dashboard view (with all stats and interactive features)
   - Event CRUD views (list, detail, create, update, delete)
   - Participant CRUD views (list, detail, create, update, delete)
   - Category CRUD views (list, detail, create, update, delete)
   - Search view for events

4. **Templates Required:**
   - base.html (with navigation and Tailwind CSS)
   - dashboard.html (with stats grid and interactive features)
   - Event templates (list, detail, form)
   - Participant templates (list, detail, form)
   - Category templates (list, detail, form)

---

## GRADING CHECKLIST

Ensure your solution includes:
- ✅ All three models with exact field specifications (15 marks)
- ✅ Complete CRUD for all models with validation (10 marks)  
- ✅ All four optimized query types implemented (10 marks)
- ✅ Responsive UI with Tailwind CSS (15 marks)
- ✅ Consistent navigation and styling (5 marks)
- ✅ Complete dashboard with interactive stats (15 marks)
- ✅ Search functionality using icontains (10 marks)

**Total: 100 Marks**

---

## IMPLEMENTATION NOTES

- Start with creating the Django project and app
- Set up Tailwind CSS integration
- Create models and run migrations
- Implement views and templates systematically
- Test all functionality thoroughly
- Ensure responsive design works on different screen sizes
- Validate all forms and error handling
- Test optimized queries and confirm they work as expected

This assignment tests Django ORM knowledge, query optimization, responsive design with Tailwind CSS, and full-stack web development skills.