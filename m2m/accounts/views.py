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
    user_name = request_vals.get('name').strip()
    address = request_vals.get('address')
    email = request_vals.get('email')
    try:
        inventory = Account.objects.get(name=user_name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The name already exists in the application'}))
    except Exception:
        pass

    account = Account.objects.create(
        name = user_name,
        address = address,
        email = email
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

@require_http_methods(['POST'])
@csrf_exempt
def update_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    account_id = request_vals.get('account_id')
    name = request_vals.get('name')
    address = request_vals.get('address')
    email = request_vals.get('email')
   
    account = Account.objects.get(pk=account_id)
    account.name = name
    account.address = address
    account.email = email
    account.save()
    
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_account(request):
    account_name = request.GET.get('account_name', '')
    accounts = Account.objects.filter(name__icontains=account_name)
    return HttpResponse(json.dumps({'response':accounts}))
