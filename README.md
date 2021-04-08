# Bug Tracker App

Bug tracker app written in python/django

## Installation

Use the package manager poetry to install bugtracker.

```bash
poetry install
poetry shell
python manage.py migrate
python manage.py runserver
```

## Features

* requires logging in, but people who aren't logged in _cannot_ create accounts (don't want any random person to see
  bugs in your application!)
* uses a custom user model to replace the built-in one
* has a homepage that shows all tickets, arranged in separate sections according to current ticket status (i.e. New, In
  Progress, Done, Invalid)
* allows filing/creating tickets
* has a ticket detail page
* allows assigning a ticket to the currently logged-in user
* allows marking a ticket as invalid
* allows marking a ticket as complete
* allows editing tickets (limited to Title and Description, do not include other any of the other fields)
* has a user detail page where you can see:
    * the current tickets assigned to a user
    * which tickets that user has filed
    * which tickets that user completed

`Ticket` model has the following fields:

* Title: str
* Time / Date filed: datetime
* Description: str
* User who filed ticket: FK (Foreign Key)
* Status of ticket: str
    * Possible statuses
        * New
        * In Progress
        * Done
        * Invalid
    * _
* User assigned to ticket: FK
* User who completed the ticket: FK

When a ticket is filed/created, it has the following settings:

* Status: New
* User Assigned: None
* User who Completed: None
* User who filed: Person who's logged in

When a ticket is assigned, these change as follows:

* Status: In Progress
* User Assigned: person the ticket now belongs to
* User who Completed: None

When a ticket is Done, these change as follows:

* Status: Done
* User Assigned: None
* User who Completed: person who the ticket used to belong to

When a ticket is marked as Invalid, these change as follows:

* Status: Invalid
* User Assigned: None
* User who Completed: None

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)