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
    account_names = ''
    m2m_accounts = Account.objects.all()
    for account in m2m_accounts:
        account_names += account.name + ','
    print account_names
    options.update({'inventories': inventories, 'inven_names':account_names})
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
    account_name = request_vals.get('account_id').strip()

    try:
        inventory = Inventory.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The name already exists in the application'}))
    except Exception:
        pass

    try:
        account = Account.objects.get(name=account_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of account is incorrectly'}))
    
    inventory = Inventory.objects.create(
        name = name,
        fuel_type = fuel_type,
        location = in_location,
        id_number = id_number,
        m2m_account = account
    )
    inventory.save()

    return HttpResponse(json.dumps({'response': 'success', 'account_id': account.id} ))

@require_http_methods(['POST'])
@csrf_exempt
def remove_inventory(request):
    request_vals = request.POST
    inventories = request_vals.getlist('inventories[]', '')

    Inventory.objects.filter(pk__in=inventories).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
def update_inventory(request):
    request_vals = request.POST
    inventory_id = request_vals.get('inventory_id')
    name = request_vals.get('name')
    fuel_type = request_vals.get('fuel_type')
    location = request_vals.get('in_location')
    id_number = request_vals.get('id_number')
    volumn = request_vals.get('volumn')

    inventory = Inventory.objects.get(pk=inventory_id)
    inventory.name = name
    inventory.fuel_type = fuel_type
    inventory.location = location
    inventory.id_number = id_number
    inventory.volumn = volumn
    inventory.save()

    return HttpResponse(json.dumps({'response': 'success'}))
