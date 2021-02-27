from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_list_or_404
from django.urls import reverse

from .forms import CreateTicketForm, EditTicketForm

from bug_tracker.models import Ticket


# Home view
def index(request):
    # Status options for ticket
    # ('New', 'New'),
    # ('In Progress', 'In Progress'),
    # ('Done', 'Done'),
    # ('Invalid', 'Invalid'),
    tickets = Ticket.objects.all().order_by('-time_created')
    tickets_new = Ticket.objects.filter(status_of_ticket='New').order_by('-time_created')
    tickets_in_progress = Ticket.objects.filter(status_of_ticket='In Progress').order_by('-time_created')
    tickets_done = Ticket.objects.filter(status_of_ticket='Done').order_by('-time_created')
    tickets_invalid = Ticket.objects.filter(status_of_ticket='Invalid').order_by('-time_created')

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
@login_required
def author_detail(request, author_id):
    author = Ticket.objects.filter(author_of_ticket=author_id)
    tickets = Ticket.objects.filter(author_of_ticket_id=author_id).order_by('-time_created')
    return render(request, 'author_detail.html', {
        'author': author.first().author_of_ticket.username,
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


@login_required
def edit_ticket(request, ticket_id):
    tickets = Ticket.objects.all()
    ticket = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data["title"]
            # ticket.status_of_ticket = data["status_of_ticket"]
            ticket.description = data["description"]
            ticket.save()
        return HttpResponseRedirect(reverse("ticket_detail", args=[ticket.id]))

    data = {
        "title": ticket.title,
        "description": ticket.description,
        # "status_of_ticket": ticket.status_of_ticket,
    }
    form = EditTicketForm(initial=data)
    return render(request, "edit_ticket.html", {"form": form})
