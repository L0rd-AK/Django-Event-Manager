from django.contrib import admin
from .models import Category, Event, Participant


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'time', 'location', 'category']
    list_filter = ['category', 'date']
    search_fields = ['name', 'location', 'description']
    ordering = ['date', 'time']
    date_hierarchy = 'date'


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event_count']
    search_fields = ['name', 'email']
    filter_horizontal = ['events']
    ordering = ['name']

    def event_count(self, obj):
        return obj.events.count()
    event_count.short_description = 'Number of Events'
