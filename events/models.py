from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """Category model as specified in Section 1.1"""
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})


class Event(models.Model):
    """Event model as specified in Section 1.2"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date', 'time']

    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'pk': self.pk})

    @property
    def is_upcoming(self):
        """Check if event is in the future"""
        return self.date >= timezone.now().date()

    @property
    def is_past(self):
        """Check if event is in the past"""
        return self.date < timezone.now().date()

    @property
    def is_today(self):
        """Check if event is today"""
        return self.date == timezone.now().date()


class Participant(models.Model):
    """Participant model as specified in Section 1.3"""
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    events = models.ManyToManyField(Event, related_name='participants', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('participant_detail', kwargs={'pk': self.pk})

    @property
    def event_count(self):
        """Get the number of events this participant is registered for"""
        return self.events.count()
