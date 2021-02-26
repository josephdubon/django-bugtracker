from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CreateTicketForm

from bug_tracker.models import Ticket


# Home view
def index(request):
    # Status options for ticket
    # ('New', 'New'),
    # ('In Progress', 'In Progress'),
    # ('Done', 'Done'),
    # ('Invalid', 'Invalid'),
    tickets = Ticket.objects.all()
    tickets_new = Ticket.objects.filter(status_of_ticket='New')
    tickets_in_progress = Ticket.objects.filter(status_of_ticket='In Progress')
    tickets_done = Ticket.objects.filter(status_of_ticket='Done')
    tickets_invalid = Ticket.objects.filter(status_of_ticket='Invalid')

    return render(request, 'home.html', {
        'heading': 'Bug Tracker App',
        'tickets': tickets,
        'tickets_new': tickets_new,
        'tickets_in_progress': tickets_in_progress,
        'tickets_done': tickets_done,
        'tickets_invalid': tickets_invalid,
    })


# Ticket detail view
@login_required
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'ticket_detail.html', {
        'ticket': ticket
    }
                  )


# Author detail view
def author_detail(request, author_id):
    author_obj = Ticket.objects.get(author_of_ticket_id=author_id)
    tickets = Ticket.objects.filter(author_of_ticket_id=author_id)
    return render(request, 'author_detail.html', {
        'author': author_obj.author_of_ticket,
        'tickets': tickets
    }
                  )


# Create ticket view
@login_required
def create_ticket(request):
    context = {}

    if request.method == "POST":
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_ticket = Ticket.objects.create(
                title=data['title'],
                author_of_ticket=request.user,
                description=data['description'],
                assignee_of_ticket=None,
                closer_of_ticket=None
            )
            if new_ticket:
                return HttpResponseRedirect(reverse('home'))

    form = CreateTicketForm()
    context.update({'form': form})
    return render(
        request,
        'create_ticket.html',
        context
    )
