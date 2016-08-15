from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from hedge_transaction.models import Hedge_Tran
from hedge_account.models import Hedge_Account
from inventory.models import Inventory
from hedge_instrument.models import Instrument
import simplejson as json
import logging



@login_required
def hedge_tran(request):
    options = {}
    hedge_trans = Hedge_Tran.objects.all()
    hedge_accounts = Hedge_Account.objects.all()
    hedge_names = ''
    for hedge in hedge_accounts:
        hedge_names += hedge.name + ','
    instrument_names = ''
    instruments = Instrument.objects.all()
    for instrument in instruments:
        instrument_names += instrument.symbol + ','
    inventory_names = ''
    invents = Inventory.objects.all()
    for invent in invents:
        inventory_names += invent.name + ','

    options.update({'hedge_trans': hedge_trans, 'hedge_list': hedge_names, 'instrument_list': instrument_names, 'invent_list':inventory_names})
    render_to_url = 'hidden/hedge_transaction.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_hedge_tran(request):
    request_vals = request.POST
    name = request_vals.get('name')
    hedge_type = request_vals.get('type')
    hedge_id = request_vals.get('hedge_account')
    inventory_id = request_vals.get('inventory')
    instrument_id = request_vals.get('contract')
    volume = request_vals.get('volume')
    price = request_vals.get('price')
    initial_pos = request_vals.get('initial_pos')
    confirm_number = request_vals.get('confirm_number')
    trader = request_vals.get('trader')
    status = request_vals.get('ht_status')
    program = request_vals.get('program')

    #hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    #instrument = Instrument.objects.get(pk=instrument_id)
    try:
        hedge_account = Hedge_Account.objects.get(name=hedge_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of hedge account is incorrectly'}))
    try:
        inventory = Inventory.objects.get(name=inventory_id)
        if ht_status.lower() == 'confirmed'
            if hedge_type.lower() == 'purchase':
                inventory.volumn += int(net_volume)
            elif hedge_type.lower() == 'sell':
                if inventory.volumn < int(net_volume):
                    return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the inventory'}))
                else:
                    inventory.volumn -= int(net_volume)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory is incorrectly'}))
    try:
        instrument = Instrument.objects.get(symbol=instrument_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of contract is incorrectly'}))

    hedge_tran = Hedge_Tran.objects.create(
        name = name,
        hedge_type = hedge_type,
        hedge_account = hedge_account,
        instrument = instrument,
        inventory = inventory,
        volume = volume,
        price = price,
        initial_pos = initial_pos,
        confirm_number = confirm_number,
        trader = trader,
        status = status,
        program = program
    )
    hedge_tran.save()
    inventory.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_ht(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    hedge_trans = request_vals.getlist('hedge_trans[]', '')
   
    Hedge_Tran.objects.filter(pk__in=hedge_trans).delete()
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_hedge_tran(request):
    request_vals = request.GET

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_ht(request):
    request_vals = request.POST
    hedge_tran_id = request_vals.get('hedge_tran_id')
    name = request_vals.get('name')
    address = request_vals.get('address')
    email = request_vals.get('email')
   
    hedge_tran = Hedge_Tran.objects.get(pk=hedge_tran_id)
    hedge_tran.name = name
    hedge_tran.address = address
    hedge_tran.email = email
    hedge_tran.save()
    
    
    return HttpResponse(json.dumps({'response': 'success'}))

