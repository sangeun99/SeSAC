from django.shortcuts import render
from django.http import HttpResponse
from .models import Message

# Create your views here.
def hello_world(request) :
    return HttpResponse("Hello World")

def show_message(request) :
    messages = Message.objects.all()
    return render(request, 'message_list.html', {'messages': messages})

   
#     new_message = Message(text="안녕히 가세요")
#     new_message.save()

#     message = Message.objects.filter(id=1).all()
#     message.delete()
