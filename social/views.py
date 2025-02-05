from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def feed(request):
    return render(request, 'social/feed.html')

@login_required
def explore(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'social/explore.html', {'users': users})

@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'social/profile.html', {'profile_user': user})

@login_required
def messages(request):
    return render(request, 'social/messages.html')

@login_required
def notifications(request):
    return render(request, 'social/notifications.html')
