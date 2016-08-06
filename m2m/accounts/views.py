from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from accounts.models import Account
from users.models import User
from django.http import HttpResponse
import simplejson as json
import logging

@csrf_exempt
def login(request):
    if request.method == 'GET':
        render_to_url = 'login.html'
        return render_to_response(render_to_url)
    else:
        print request.method
        print request
        print request.POST
        if 'username' in request.POST:
            username = request.POST['username']
        if 'password' in request.POST:
            password = request.POST['password']
        try:
            User.objects.get(name=username, password=password)
            return HttpResponseRedirect('/')
        except Exception:
            return 

@login_required
def index(request):
    print request.user
    print request.user.id
    options = {}
    options.update({'username': request.user})
    render_to_url = 'value/value.html'
    return render_to_response(render_to_url)

@login_required
def accounts(request):
    options = {}
    try:
        if request.user.user_privilages.code == 1:
            accounts = Account.objects.all()
        else:
            
#        user = User.objects.get(pk=request.user.id)
            accounts = Account.objects.filter(user = request.user)
    except Exception:
        accounts = {}
    options.update({'accounts': accounts})
    render_to_url = 'hidden/account.html'
    return render_to_response(render_to_url, options)
def log(request):
    render_to_url = 'transactions_log.html'
    return render_to_response(render_to_url)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    user_name = request_vals.get('name').strip()
    address = request_vals.get('address')
    email = request_vals.get('email')
    user_id = request.user.id
    try:
        account = Account.objects.get(name=user_name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The name already exists in the application'}))
    except Exception:
        pass

    user = User.objects.get(pk=user_id)

    account = Account.objects.create(
        name = user_name,
        address = address,
        email = email,
        user = user
    )
    account.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
@login_required
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
@login_required
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

