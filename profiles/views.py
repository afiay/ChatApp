# In profiles/views.py

from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Profile


from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render


def profile_list(request):
    # Get the query parameter 'q' from the URL, default to an empty string if not present
    query = request.GET.get("q", "")
    # Filter users by the query parameter, excluding the logged-in user
    users = User.objects.exclude(id=request.user.id).filter(
        Q(username__icontains=query))
    return render(request, 'profiles/profile_list.html', {'users': users, 'query': query})
