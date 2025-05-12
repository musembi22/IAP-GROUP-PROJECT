from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page - event list
    path('', views.event_list, name='event_list'),

    # Create event
    path('create/', views.create_event, name='create_event'),

    # RSVP
    path('rsvp/<int:event_id>/', views.rsvp_event, name='rsvp_event'),

    # Signup page
    path('signup/', views.signup, name='signup'),

    # Delete event
    path('delete/<int:event_id>/', views.delete_event, name='delete_event'),

    # ✅ Logout redirects to signup page
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='signup'), name='logout'),
]
