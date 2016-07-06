from django.shortcuts import render, render_to_response
from users.models import User

def users(request):
    options = {}
    users = User.objects.all()
    options.update({'users': users})
    render_to_url = 'hidden/users.html'
    return render_to_response(render_to_url, options)

