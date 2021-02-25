"""
Title: str
Time / Date filed: datetime
Description: str
User who filed ticket: FK (Foreign Key)
Status of ticket: str
    Possible statuses
    New
    In Progress
    Done
    Invalid
    hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
User assigned to ticket: FK
User who completed the ticket: FK

"""

from django.conf import settings
from django.db import models
from django.utils import timezone


# Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=350)
    time_created = models.DateTimeField(default=timezone.now, blank=True)
    author_of_ticket = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status_of_ticket = ''
    # new, in_progress, done, invalid
    assignee_of_ticket = ''
    closer_of_ticket = ''

    def __str__(self):
        return f'{self.title} | {self.description} | {self.author_of_ticket}'
