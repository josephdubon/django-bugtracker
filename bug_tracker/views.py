from django.shortcuts import render

from bug_tracker.models import Ticket


# Home view
def index(request):
    tickets = Ticket.objects.all()
    return render(request, 'home.html', {
        'heading': 'Bug Tracker App',
        'tickets': tickets,
    })


# Ticket detail view
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
