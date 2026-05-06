from django.http import HttpResponse
from .models import Message

def home(request):
    messages = Message.objects.all()
    output = "Messages:<br>"
    for msg in messages:
        output += msg.text + "<br>"
    return HttpResponse(output)

def about(request):
    html = """
    <h1>About</h1>
    <p>This is a simple Django demo app built for Breakout #3.</p>
    <p>It demonstrates the Model-View-Template pattern using Django 4.2.</p>
    <br>
    <a href="/">Back to Home</a>
    """
    return HttpResponse(html)
