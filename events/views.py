from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from .models import Category, Event, Participant
from .forms import CategoryForm, EventForm, ParticipantForm, EventSearchForm


# Health check endpoint
def health_check(request):
    """Simple health check to verify the app is working"""
    try:
        # Test database connection
        db_status = "OK"
        count = Event.objects.count()
        
        return JsonResponse({
            'status': 'healthy',
            'database': db_status,
            'event_count': count,
            'debug': getattr(settings, 'DEBUG', False)
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'error': str(e)
        }, status=500)


# Dashboard View (Section 4.3)
def dashboard(request):
    """Comprehensive dashboard with stats and interactive features"""
    try:
        # Stats for the dashboard (Section 3.3 - Aggregate queries)
        total_participants = Participant.objects.aggregate(
            total=Count('id')
        )['total'] or 0
        
        total_events = Event.objects.count()
        
        # Upcoming and past events
        today = timezone.now().date()
        upcoming_events = Event.objects.filter(date__gte=today).count()
        past_events = Event.objects.filter(date__lt=today).count()
        
        # Today's events
        today_events = Event.objects.filter(date=today).select_related('category').prefetch_related('participants')
        
        # Filter for interactive stats
        filter_type = request.GET.get('filter', 'all')
        if filter_type == 'upcoming':
            events = Event.objects.filter(date__gte=today).select_related('category').prefetch_related('participants')
        elif filter_type == 'past':
            events = Event.objects.filter(date__lt=today).select_related('category').prefetch_related('participants')
        else:
            events = Event.objects.all().select_related('category').prefetch_related('participants')
    except Exception as e:
        # Handle database errors gracefully
        total_participants = 0
        total_events = 0
        upcoming_events = 0
        past_events = 0
        today_events = []
        events = []
        filter_type = 'all'
        # Log the error for debugging
        print(f"Dashboard error: {e}")
    
    context = {
        'total_participants': total_participants,
        'total_events': total_events,
        'upcoming_events': upcoming_events,
        'past_events': past_events,
        'today_events': today_events,
        'events': events[:10],  # Limit to 10 for display
        'filter_type': filter_type,
    }
    
    # AJAX response for interactive stats
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'events': [
                {
                    'name': event.name,
                    'date': event.date.strftime('%Y-%m-%d'),
                    'time': event.time.strftime('%H:%M'),
                    'location': event.location,
                    'category': event.category.name,
                    'participants_count': event.participants.count(),
                    'url': event.get_absolute_url()
                }
                for event in events[:10]
            ]
        })
    
    return render(request, 'events/dashboard.html', context)


# Event Views (Section 2.1 & 3)
class EventListView(ListView):
    """Event list view with optimized queries and search functionality"""
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 12

    def get_queryset(self):
        # Section 3.1 - select_related usage for optimization
        queryset = Event.objects.select_related('category').prefetch_related('participants')
        
        # Section 5 - Search functionality
        form = EventSearchForm(self.request.GET)
        if form.is_valid():
            search_query = form.cleaned_data.get('search_query')
            category = form.cleaned_data.get('category')
            date_from = form.cleaned_data.get('date_from')
            date_to = form.cleaned_data.get('date_to')
            
            if search_query:
                # Section 5.2 - icontains lookup for case-insensitive search
                queryset = queryset.filter(
                    Q(name__icontains=search_query) | 
                    Q(location__icontains=search_query)
                )
            
            if category:
                queryset = queryset.filter(category=category)
            
            # Section 3.4 - Date range filter
            if date_from:
                queryset = queryset.filter(date__gte=date_from)
            if date_to:
                queryset = queryset.filter(date__lte=date_to)
        
        return queryset.order_by('date', 'time')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = EventSearchForm(self.request.GET)
        context['search_query'] = self.request.GET.get('search_query', '')
        return context


class EventDetailView(DetailView):
    """Event detail view with optimized queries"""
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_queryset(self):
        # Section 3.2 - prefetch_related for participants
        return Event.objects.select_related('category').prefetch_related('participants')


class EventCreateView(CreateView):
    """Event create view with form validation"""
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Event "{form.instance.name}" was created successfully!')
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    """Event update view with form validation"""
    model = Event
    form_class = EventForm
    template_name = 'events/event_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Event "{form.instance.name}" was updated successfully!')
        return super().form_valid(form)


class EventDeleteView(DeleteView):
    """Event delete view with confirmation"""
    model = Event
    template_name = 'events/event_confirm_delete.html'
    success_url = reverse_lazy('event_list')

    def delete(self, request, *args, **kwargs):
        event_name = self.get_object().name
        messages.success(request, f'Event "{event_name}" was deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Category Views (Section 2.3)
class CategoryListView(ListView):
    """Category list view"""
    model = Category
    template_name = 'events/category_list.html'
    context_object_name = 'categories'
    paginate_by = 12

    def get_queryset(self):
        return Category.objects.annotate(event_count=Count('event')).order_by('name')


class CategoryDetailView(DetailView):
    """Category detail view with related events"""
    model = Category
    template_name = 'events/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get events in this category with optimized queries
        context['events'] = Event.objects.filter(category=self.object).select_related('category').prefetch_related('participants').order_by('date', 'time')
        return context


class CategoryCreateView(CreateView):
    """Category create view"""
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Category "{form.instance.name}" was created successfully!')
        return super().form_valid(form)


class CategoryUpdateView(UpdateView):
    """Category update view"""
    model = Category
    form_class = CategoryForm
    template_name = 'events/category_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Category "{form.instance.name}" was updated successfully!')
        return super().form_valid(form)


class CategoryDeleteView(DeleteView):
    """Category delete view with confirmation"""
    model = Category
    template_name = 'events/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def delete(self, request, *args, **kwargs):
        category_name = self.get_object().name
        messages.success(request, f'Category "{category_name}" was deleted successfully!')
        return super().delete(request, *args, **kwargs)


# Participant Views (Section 2.2)
class ParticipantListView(ListView):
    """Participant list view"""
    model = Participant
    template_name = 'events/participant_list.html'
    context_object_name = 'participants'
    paginate_by = 12

    def get_queryset(self):
        return Participant.objects.prefetch_related('events').order_by('name')


class ParticipantDetailView(DetailView):
    """Participant detail view with events"""
    model = Participant
    template_name = 'events/participant_detail.html'
    context_object_name = 'participant'

    def get_queryset(self):
        return Participant.objects.prefetch_related('events__category')


class ParticipantCreateView(CreateView):
    """Participant create view"""
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Participant "{form.instance.name}" was created successfully!')
        return super().form_valid(form)


class ParticipantUpdateView(UpdateView):
    """Participant update view"""
    model = Participant
    form_class = ParticipantForm
    template_name = 'events/participant_form.html'

    def form_valid(self, form):
        messages.success(self.request, f'Participant "{form.instance.name}" was updated successfully!')
        return super().form_valid(form)


class ParticipantDeleteView(DeleteView):
    """Participant delete view with confirmation"""
    model = Participant
    template_name = 'events/participant_confirm_delete.html'
    success_url = reverse_lazy('participant_list')

    def delete(self, request, *args, **kwargs):
        participant_name = self.get_object().name
        messages.success(request, f'Participant "{participant_name}" was deleted successfully!')
        return super().delete(request, *args, **kwargs)
