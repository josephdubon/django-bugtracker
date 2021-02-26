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
    TICKET_STATUS = [
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]

    title = models.CharField(max_length=50)
    description = models.TextField(max_length=350)
    time_created = models.DateTimeField(default=timezone.now, blank=True)
    status_of_ticket = models.CharField(max_length=24, choices=TICKET_STATUS, default='New')
    author_of_ticket = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name='author_of_ticket', null=True)
    assignee_of_ticket = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='assignee_of_ticket')
    closer_of_ticket = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True,
                                         related_name='closer_of_ticket')

    def __str__(self):
        return f'{self.title} | {self.description} | {self.author_of_ticket}'
