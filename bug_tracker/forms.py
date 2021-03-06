from django import forms


class CreateTicketForm(forms.Form):
    title = forms.CharField(max_length=40)
    description = forms.CharField(widget=forms.Textarea, max_length=250)


class EditTicketForm(forms.Form):
    TICKET_STATUS = [
        ('---', '---'),
        ('New', 'New'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
        ('Invalid', 'Invalid'),
    ]

    title = forms.CharField(max_length=50)
    status_of_ticket = forms.ChoiceField(choices=TICKET_STATUS)
    description = forms.CharField(max_length=350)