from django.shortcuts import render, redirect
from .models import Message

def chat_view(request):
    messages = Message.objects.all()
    return render(request, 'chat.html', {'messages': messages})

def send_message(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        content = request.POST.get('content')
        if username and content:
            Message.objects.create(username=username, content=content)
    return redirect('chat_room')  # Corrected name to 'chat_room'

def clear_chat(request):
    if request.method == 'GET':
        Message.objects.all().delete()  # Clear all messages from the chat
        return redirect('chat_room')  # Redirect back to the chat room page

