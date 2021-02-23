"""
Models with the appropriate fields
Each ticket should have the following fields:

Title
Time / Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid)
Name of user assigned to ticket
Name of user who completed the ticket
"""

import datetime

from django.db import models


# Ticket model
class Ticket(models.Model):
    title = models.CharField(max_length=150)
    time_created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    description = models.TextField(max_length=350)
    # look at comment above to finish model archetype
    pass
