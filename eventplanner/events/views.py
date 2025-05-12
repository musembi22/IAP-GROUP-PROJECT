from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Event, RSVP

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})

@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        date = request.POST['date']
        time = request.POST['time']
        event = Event(
            title=title,
            description=description,
            location=location,
            date=date,
            time=time,
            organizer=request.user
        )
        event.save()
        return redirect('event_list')
    return render(request, 'events/create_event.html')

@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    RSVP.objects.get_or_create(user=request.user, event=event)
    return redirect('event_list')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('event_list')
    else:
        form = UserCreationForm()
    return render(request, 'events/signup.html', {'form': form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if event.organizer != request.user:
        messages.error(request, "You are not authorized to delete this event.")
        return redirect('event_list')

    if request.method == 'POST':
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect('event_list')

    return render(request, 'events/delete_event.html', {'event': event})
