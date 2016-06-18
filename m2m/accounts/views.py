from django.shortcuts import render, render_to_response


def index(request):

    render_to_url = 'index.html'
    return render_to_response(render_to_url)

# Create your views here.
