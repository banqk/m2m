from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from inventory.models import Inventory
from accounts.models import Account
import simplejson as json


def inventories(request):
    options = {}
    inventories = Inventory.objects.all()
    options.update({'inventories': inventories})
    render_to_url = 'hidden/inventory.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_inventory(request):
    request_vals = request.POST
    name = request_vals.get('name')
    fuel_type = request_vals.get('fuel_type')
    in_location = request_vals.get('in_location')
    id_number = request_vals.get('id_number')
    account_id = request_vals.get('account_id')
    print account_id

    account = Account.objects.get(pk=account_id)
    
    inventory = Inventory.objects.create(
        name = name,
        fuel_type = fuel_type,
        location = in_location,
        id_number = id_number,
        m2m_account = account
    )
    inventory.save()

    return HttpResponse(json.dumps({'response': 'success', 'account_id':account_id } ))

@require_http_methods(['POST'])
@csrf_exempt
def remove_inventory(request):
    request_vals = request.POST
    inventories = request_vals.getlist('inventories[]', '')

    Inventory.objects.filter(pk__in=inventories).delete()

    return HttpResponse(json.dumps({'response': 'success'}))
