from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from events.models import Category, Event, Participant
from django.utils import timezone
from datetime import date, time


class Command(BaseCommand):
    help = 'Create sample data for the event management system'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories
        categories_data = [
            {'name': 'Technology', 'description': 'Technology and programming events'},
            {'name': 'Business', 'description': 'Business and entrepreneurship events'},
            {'name': 'Education', 'description': 'Educational and academic events'},
            {'name': 'Health', 'description': 'Health and wellness events'},
        ]
        
        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')
        
        # Create events
        events_data = [
            {
                'name': 'Django Workshop',
                'description': 'Learn Django web development',
                'date': date(2025, 9, 15),
                'time': time(10, 0),
                'location': 'Tech Center',
                'category': categories[0]
            },
            {
                'name': 'Startup Pitch Competition',
                'description': 'Present your startup ideas',
                'date': date(2025, 9, 20),
                'time': time(14, 0),
                'location': 'Business Hub',
                'category': categories[1]
            },
        ]
        
        events = []
        for event_data in events_data:
            event, created = Event.objects.get_or_create(
                name=event_data['name'],
                defaults=event_data
            )
            events.append(event)
            if created:
                self.stdout.write(f'Created event: {event.name}')
        
        # Create participants
        participants_data = [
            {'name': 'John Doe', 'email': 'john@example.com'},
            {'name': 'Jane Smith', 'email': 'jane@example.com'},
        ]
        
        for part_data in participants_data:
            participant, created = Participant.objects.get_or_create(
                email=part_data['email'],
                defaults={'name': part_data['name']}
            )
            if created:
                # Add participant to some events
                participant.events.add(*events[:1])
                self.stdout.write(f'Created participant: {participant.name}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )
