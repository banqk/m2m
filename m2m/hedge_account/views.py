from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from hedge_account import Hedge_Account
import simplejson as json


def hedges(request):
    options = {}
    hedges = Hedge_Account.objects.all()
    options.update({'hedges': hedges})
    render_to_url = 'hidden/single_account.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_hedge_account(request):
    request_vals = request.POST
    name = request_vals.get('name')
    institution = request_vals.get('institution')
    account_number = request_vals.get('account_number')

    hedge = Hedge_Account.objects.create(
        name = name,
        institution = institution,
        id_number = account_number
    )
    hedge.save()

    return HttpResponse(json.dumps({'response': 'success'}))
