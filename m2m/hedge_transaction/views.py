from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from hedge_transaction.models import Hedge_Tran, Hedge_Price
from hedge_account.models import Hedge_Account
from inventory.models import Inventory, HedgePos, SellPrice
from product.models import Product
from hedge_instrument.models import Instrument
from fuel_class.models import Fuel_Class
import simplejson as json
import logging
import urllib2
import time


@login_required
def hedge_tran(request):
    options = {}

    products = Product.objects.all()
    product_names = ''
    for product in products:
        product_names += product.name + ','

    instruments = Instrument.objects.all()
    instrument_names = ''
    for instrument in instruments:
        instrument_names += instrument.instrument + ','
    print instrument_names

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
    options.update({'hedge_trans': hedge_trans, 'hedge_account_list': hedge_names, 'invent_list': inventory_names, 'product_list':product_names, 'instrument_list':instrument_names})
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
    product_name = request_vals.get('product')
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
    print hedge_type.lower() + 'aaaaaaaaa'
    print inventory_name + '!!!!!'
    print product_name
    try:
        hedge_account = Hedge_Account.objects.get(name=hedge_id)
        inventory = Inventory.objects.get(name=inventory_name)
        product = Product.objects.get(name=product_name)
        sell_price = SellPrice.objects.get(inventory=inventory,product=product)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of hedge account is incorrectly'}))
    try:
        inventory = Inventory.objects.get(name=inventory_name)
        product = Product.objects.get(name=product_name)
        sell_price = SellPrice.objects.get(inventory=inventory,product=product)
        #hedge_pos = HedgePos.objects.filter(inventory=inventory)
        if status.lower() == 'confirmed':
            if hedge_type.lower() == 'purchase':
                sell_price.volume += int(volume)
            elif hedge_type.lower() == 'sell':
#                if sell_price.volume < int(volume):
#                    return HttpResponse(json.dumps({'response':'faliure', 'info':'The volume greater than the inventory'}))
#                else:
                sell_price.volume -= int(volume)
#            else:
#                to_inventory = request_vals.get('to_inventory')
#                try:
#                    to_invent = Inventory.objects.get(name=to_inventory)
#                    to_invent.volumn += int(volume)
#                    inventory.volumn -= int(volume)
#                except Exception:
#                    return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of to inventory is incorrectly'}))
#"""
#            try:
#                hedge_pos = HedgePos.objects.get(inventory=inventory, product=product)
#                now_pos = hedge_pos.position
#                hedge_pos.position = hedge_pos.position + position
#                hedge_pos.last_price = hedge_pos.price
                #now_price = hedge_pos.price
                #hedge_pos.price = (now_price*now_pos + float(price) * int(volume))/hedge_pos.position
#                hedge_pos.price = price
#            except Exception as e:
#                print e
#                hedge_pos = HedgePos.objects.create(
#                    inventory = inventory,
#                    product = product,
#                    position = position,
#                    last_price = price,
#                    price = price
#                )
#"""
    except Exception, e:
        print e
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory is incorrectly'}))
    try:
        instrument = Instrument.objects.get(instrument=instrument_id)
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
    print hedge_tran.id
    if hedge_type.lower() == 'purchase':
        position = int(volume)
    elif hedge_type.lower() == 'sell':
        position = -int(volume)
        sell_price.hedge_price = price
    try:
	one_pos = HedgePos.objects.filter(inventory=inventory, product=product).latest('id')
	position = one_pos.position + position
	#now_price = hedge_pos.price
	#hedge_pos.price = (now_price*now_pos + float(price) * int(volume))/hedge_pos.position
	#hedge_pos.price = price
        one_pos.status = 'CLOSED'
        print one_pos.status
        if position == 0:
            status = 'CLOSED'
        else:
            status = 'OPEN'
	hedge_pos = HedgePos.objects.create(
	    inventory = inventory,
	    product = product,
	    position = position,
	    last_price = price,
	    price = price,
            status = status
	)
        one_pos.save()
        hedge_pos.save()
    except Exception as e:
	print e
	hedge_pos = HedgePos.objects.create(
	    inventory = inventory,
	    product = product,
	    position = position,
	    last_price = price,
	    price = price,
            status = 'OPEN'
	)
        hedge_pos.save()

    sell_price.hedge_volume += position
#    sell_price.hedge_price = price
    sell_price.save()
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


#@require_http_methods(['POST'])
#@csrf_exempt
#@login_required
def hedge_pos(request):
    options = {}
#    inventories = Inventory.objects.all()
#    hedge_trans = Hedge_Tran.objects.all()
#    hedge_invs = [x.inventory for x in hedge_trans]
    rows = []

#    for inv in inventories:
    hedge_pos = HedgePos.objects.all()
    #data1 = get_request_data('HOZ2016')
    #data2 = get_request_data('RBZ2016')
    current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()-2*24*3600))
    print current_date
    one_hedge = Hedge_Price.objects.filter(h_date=str(current_date), h_type='HOZ2016')
    now_price = 0
    for one in one_hedge:
        print one.h_settle
        now_price = one.h_settle
        break
    for h in hedge_pos:
        data = {}
    
        sell_price = SellPrice.objects.get(inventory=h.inventory, product=h.product)
        data['name'] = h.inventory.name
        data['product_name'] = h.product.name
        #data['volume'] = h.inventory.volumn
        data['volume'] = sell_price.volume
#        if inv in hedge_invs:
#            ht = [x for x in hedge_trans if x.inventory.name == inv.name][0]
        data['pos'] = h.position
        data['price'] = h.price
        data['margin'] = now_price - h.price 
        data['overview'] = (now_price - h.price) * sell_price.volume
        data['summary'] = 0
        data['cost_stats'] = sell_price.avg_price
        data['create_date'] = h.create_date
#        data1 = get_request_data('HOZ2016')
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


#@require_http_methods(['POST'])
#@csrf_exempt
#@login_required
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
    margin_col = [
    'Inventory Name',
    'Product Name',
    'Margin',
    'Volume',
    'Current Price',
    'Transaction Price',
    'Type'
    ]
    #data1 = get_request_data('HOZ2016')
    #data2 = get_request_data('RBZ2016')
    types = ['HOZ2016', 'RBZ2016']
    price_list = {}
    margin_list = {}
    rows = []
    for t in types:
        print t
        data1 = get_request_data(t)
        #data1.reverse()
        price_list[t] = data1
        
        hedge_pos = HedgePos.objects.all()
        for h in hedge_pos:
            data = {}
    
            code = h.product.fuel_class.code
            if code == t[0:2]:
                sell_price = SellPrice.objects.get(inventory=h.inventory, product=h.product)
                data['name'] = h.inventory.name
                data['product_name'] = h.product.name
                data['margin'] = data1[0][6] - h.price 
                data['f_type'] = t
                data['volume'] = sell_price.hedge_volume
                data['current_price'] = data1[0][6]
                data['trans_price'] = h.price
                rows.append(data)
            else:
                continue
        margin_list[t] = rows
        for d in data1:
            hedge_price = Hedge_Price.objects.create(
                h_date = d[0],
                h_open = d[1],
                h_high = d[2],
                h_low = d[3],
                h_last = d[4],
                h_change = d[5],
                h_settle = d[6],
                h_volume = d[7],
                h_interest = d[8],
                h_type = t,
            )
            hedge_price.save()
            print d
    print price_list
    data1 = price_list[types[0]]
    data2 = price_list[types[1]]

    options.update({'col_names': col_names, 'data1': data1, 'data2': data2})
    options.update({'settle_price1': data1[0][6], 'settle_price2': data2[0][6]})
    options.update({'settle_price_y1': data1[1][6], 'settle_price_y2': data2[1][6]})
    options.update({'margin_col': margin_col,'margin_list': rows})
    render_to_url = 'hidden/hedge_price.html'
    return render_to_response(render_to_url, options)


def get_request_data(market):
    api = ('https://www.quandl.com/api/v3/datasets/CME/%s.json') % market
    result = urllib2.urlopen(api)
    content = json.loads(result.read())
    data = content['dataset']['data'][0:10]
    return data

#@require_http_methods(['POST'])
#@csrf_exempt
#@login_required
def hedge_pos_view(request):
    options = {}
#    inventories = Inventory.objects.all()
#    hedge_trans = Hedge_Tran.objects.all()
#    hedge_invs = [x.inventory for x in hedge_trans]
    rows = []

#    for inv in inventories:
    hedge_pos = HedgePos.objects.all()
    current_date = time.strftime('%Y-%m-%d',time.localtime(time.time()-2*24*3600))
    print current_date
    one_hedge = Hedge_Price.objects.filter(h_date=str(current_date), h_type='HOZ2016')
    now_price = 0
    for one in one_hedge:
        print one.h_settle
        now_price = one.h_settle
        break
    for h in hedge_pos:
        data = {}
    
        sell_price = SellPrice.objects.get(inventory=h.inventory, product=h.product)
        data['name'] = h.inventory.name
        data['product_name'] = h.product.name
        #data['volume'] = h.inventory.volumn
        data['volume'] = sell_price.volume
#        if inv in hedge_invs:
#            ht = [x for x in hedge_trans if x.inventory.name == inv.name][0]
        data['pos'] = h.position
        data['price'] = h.price
        data['margin'] = now_price - h.price 
        data['overview'] = (now_price - h.price) * sell_price.volume
        data['summary'] = 0
        data['cost_stats'] = sell_price.avg_price
        data['status'] = h.status
        data['create_date'] = h.create_date
#        data1 = get_request_data('HOZ2016')
        rows.append(data)
    '''
    try:
        hedge_tran = Hedge_Tran.objects.get(pk=hedge_tran_id)
    except Hedge_Tran.DoesNotExist:
        hedge_tran = {}
    '''

    options.update({'data': rows})
    render_to_url = 'hidden/hedge_pos_view.html'
    return render_to_response(render_to_url, options)
