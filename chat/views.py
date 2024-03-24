from django.shortcuts import render, redirect

from profiles.models import Profile

def chat_page(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    context = {}
    return render(request, "chat/chatPage.html", context)

# In your views.py (e.g., chat/views.py)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Message, User


def send_message(request, user_id):
    recipient = get_object_or_404(User, id=user_id)
    if request.method == "POST":
        message_content = request.POST.get("message")
        Message.objects.create(sender=request.user,
                               recipient=recipient, message=message_content)
        return redirect('send_message', user_id=user_id)

    messages = Message.objects.filter(sender=request.user, recipient=recipient) | \
        Message.objects.filter(sender=recipient, recipient=request.user)
    messages = messages.order_by('timestamp')

    profiles = Profile.objects.exclude(user=request.user)

    search_query = request.GET.get("search", "")
    if search_query:
        profiles = profiles.filter(user__username__icontains=search_query)

    return render(request, 'chat/send_message.html', {
        'messages': messages,
        'recipient': recipient,
        'profiles': profiles,
        'search_query': search_query  # Include the search query in the context
    })
