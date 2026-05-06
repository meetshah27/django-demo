from django.http import HttpResponse
from .models import Message

def home(request):
    messages = Message.objects.all()
    output = "Messages:<br>"
    for msg in messages:
        output += msg.text + "<br>"
    return HttpResponse(output)
