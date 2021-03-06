"""
config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    The URLs provided by auth are:

        accounts/login/ [name='login']
        accounts/logout/ [name='logout']
        accounts/password_change/ [name='password_change']
        accounts/password_change/done/ [name='password_change_done']
        accounts/password_reset/ [name='password_reset']
        accounts/password_reset/done/ [name='password_reset_done']
        accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
        accounts/reset/done/ [name='password_reset_complete']
"""
from django.contrib import admin
from django.urls import path, include
from bug_tracker import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tickets/<int:ticket_id>/', views.ticket_detail, name='ticket_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
    path('create-ticket/', views.create_ticket, name='create_ticket'),
    path('edit-ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),

]
