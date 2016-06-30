from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from accounts.models import Account
from django.http import HttpResponse
import simplejson as json
import logging


def index(request):
    render_to_url = 'value/value.html'
    return render_to_response(render_to_url)

def accounts(request):
    options = {}
    accounts = Account.objects.all()
    options.update({'accounts': accounts})
    render_to_url = 'hidden/account.html'
    return render_to_response(render_to_url, options)
def log(request):
    render_to_url = 'transactions_log.html'
    return render_to_response(render_to_url)

@require_http_methods(['POST'])
@csrf_exempt
def create_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    user_name = request_vals.get('user_name')
#    password = request_vals.get('password')
    full_name = request_vals.get('full_name')
    email = request_vals.get('email')
    company = request_vals.get('company')

    account = Account.objects.create(
        name = user_name,
#        password = password,
        full_name = full_name,
        email = email,
        company = company
    )
    account.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
def remove_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    accounts = request_vals.getlist('accounts[]', '')
   
    Account.objects.filter(pk__in=accounts).delete()
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_account(request):
    request_vals = request.GET
