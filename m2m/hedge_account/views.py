from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from hedge_account.models import Hedge_Account
from accounts.models import Account
import simplejson as json


def hedges(request):
    options = {}
    hedges = Hedge_Account.objects.all()
    options.update({'hedges': hedges})
    render_to_url = 'hidden/hedge_account.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_hedge_account(request):
    request_vals = request.POST
    name = request_vals.get('name')
    institution = request_vals.get('institution')
    account_number = request_vals.get('account_number')
    account_id = request_vals.get('account_id')
    print account_id
    account = Account.objects.get(pk=account_id)

    hedge = Hedge_Account.objects.create(
        name = name,
        institution = institution,
        id_number = account_number,
        m2m_account = account
    )
    hedge.save()

    return HttpResponse(json.dumps({'response': 'success', 'account_id': account_id}))

@require_http_methods(['POST'])
@csrf_exempt
def remove_hedge_account(request):
    request_vals = request.POST
    hedge_accounts = request_vals.getlist('hedge_accounts[]', '')

    Hedge_Account.objects.filter(pk__in=hedge_accounts).delete()

    return HttpResponse(json.dumps({'response': 'success'}))
