from django.shortcuts import render, render_to_response
from accounts.models import Account
def companies(request):
    options = {}
    accounts = Account.objects.all()
    options.update({'companies': accounts})
    render_to_url = 'hidden/company.html'
    return render_to_response(render_to_url, options)

# Create your views here.
