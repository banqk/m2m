from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from hedge_account.models import Hedge_Account
from accounts.models import Account
from users.models import User
import simplejson as json


@login_required
def hedges(request):
    options = {}
    hedges = Hedge_Account.objects.all()
    m2m_accounts = Account.objects.all()
    account_names = ''
    try:
        if request.user.user_privilages.code == 1:
            hedges = Hedge_Account.objects.all()
            m2m_accounts = Account.objects.all()
        else:
            user = User.objects.filter(pk=request.user.id)
            m2m_accounts = Account.objects.filter(user = user)
            hedges = Hedge_Account.objects.filter(m2m_account__in=m2m_accounts)
    except Exception:
            hedges = []
    for account in m2m_accounts:
        account_names += account.name + ','
    print account_names
    options.update({'hedges': hedges, 'account_names': account_names})
    render_to_url = 'hidden/hedge_account.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_hedge_account(request):
    request_vals = request.POST
    name = request_vals.get('name')
    institution = request_vals.get('institution')
    account_number = request_vals.get('account_number')
    account_id = request_vals.get('account_id')
    print account_id
    try:
        hedge_account = Hedge_Account.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The name already exists in the application'}))
    except Exception:
        pass

    try:
        account = Account.objects.get(name=account_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of account is incorrectly'}))

    hedge = Hedge_Account.objects.create(
        name = name,
        institution = institution,
        id_number = account_number,
        m2m_account = account
    )
    hedge.save()

    return HttpResponse(json.dumps({'response': 'success', 'account_id': account.id}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_hedge_account(request):
    request_vals = request.POST
    hedge_accounts = request_vals.getlist('hedge_accounts[]', '')

    Hedge_Account.objects.filter(pk__in=hedge_accounts).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_hedge_account(request):
    request_vals = request.POST
    hedge_id = request_vals.get('hedge_id')
    name = request_vals.get('name')
    institution = request_vals.get('institution')
    id_number = request_vals.get('id_number')

    hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    hedge_account.name = name
    hedge_account.institution = institution
    hedge_account.id_number = id_number
    hedge_account.save()

    return HttpResponse(json.dumps({'response': 'success'}))
