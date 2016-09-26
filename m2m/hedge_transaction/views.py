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
import urllib2


@login_required
def hedge_tran(request):
    options = {}
    hedge_trans = Hedge_Tran.objects.all()

    hedge_accounts = Hedge_Account.objects.all()
    hedge_names = ''
    for hedge in hedge_accounts:
        hedge_names += hedge.name + ','
    #instrument_names = ''
    #instruments = Instrument.objects.all()
    #for instrument in instruments:
    #    instrument_names += instrument.symbol + ','
    inventory_names = ''
    invents = Inventory.objects.all()
    for invent in invents:
        inventory_names += invent.name + ','
    print hedge_names
    options.update({'hedge_trans': hedge_trans, 'hedge_account_list': hedge_names, 'invent_list': inventory_names})
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
    inventory_name = request_vals.get('inventory')
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
    to_inventory = ''
    try:
        hedge_account = Hedge_Account.objects.get(name=hedge_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of hedge account is incorrectly'}))
    try:
        inventory = Inventory.objects.get(name=inventory_name)
        if status.lower() == 'confirmed':
            if hedge_type.lower() == 'purchase':
                inventory.volumn += int(volume)
            elif hedge_type.lower() == 'sell':
                if inventory.volumn < int(volume):
                    return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the inventory'}))
                else:
                    inventory.volumn -= int(volume)
            else:
                to_inventory = request_vals.get('to_inventory')
                try:
                    to_invent = Inventory.objects.get(name=to_inventory)
                    to_invent.volumn += int(volume)
                    inventory.volumn -= int(volume)
                except Exception:
                    return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of to inventory is incorrectly'}))
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
       # to_inventory = to_invetory
    )
    hedge_tran.save()
    inventory.save()
    if hedge_type.lower == 'transfer':
        to_invent.save()
    
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


def hedge_pos(request):
    options = {}
    inventories = Inventory.objects.all()
    hedge_trans = Hedge_Tran.objects.all()
    hedge_invs = [x.inventory for x in hedge_trans]
    rows = []

    for inv in inventories:
        data = {}
        data['name'] = inv.name
        data['volume'] = inv.volumn
        if inv in hedge_invs:
            ht = [x for x in hedge_trans if x.inventory.name == inv.name][0]
            data['pos'] = ht.volume
            data['price'] = ht.price
        else:
            data['pos'] = 0
            data['price'] = 0
        rows.append(data)
    '''
    try:
        hedge_tran = Hedge_Tran.objects.get(pk=hedge_tran_id)
    except Hedge_Tran.DoesNotExist:
        hedge_tran = {}
    '''

    options.update({'data': rows})
    render_to_url = 'hidden/hedge_pos.html'
    return render_to_response(render_to_url, options)


def hedge_price(request):
    options = {}
    col_names = [
        "Date",
        "Open",
        "High",
        "Low",
        "Last",
        "Change",
        "Settle",
        "Volume",
        "Open Interest"
    ]
    data1 = get_request_data('HOZ2016')
    data2 = get_request_data('RBZ2016')

    options.update({'col_names': col_names, 'data1': data1, 'data2': data2})
    options.update({'settle_price1': data1[0][6], 'settle_price2': data2[0][6]})
    options.update({'settle_price_y1': data1[1][6], 'settle_price_y2': data2[1][6]})
    render_to_url = 'hidden/hedge_price.html'
    return render_to_response(render_to_url, options)


def get_request_data(market):
    api = ('https://www.quandl.com/api/v3/datasets/CME/%s.json') % market
    result = urllib2.urlopen(api)
    content = json.loads(result.read())
    data = content['dataset']['data'][0:10]
    return data