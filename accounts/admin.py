from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # Admin override users list view
    list_display = [
        'username',
        'homepage',
        'email',
    ]

    # Admin additional change user fields
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'displayname',
            'homepage',
        )}),
    )

    # Admin additional add user fields
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            'displayname',
            'homepage',
            'email',
        )}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.site_header = "Bug Tracker App"
