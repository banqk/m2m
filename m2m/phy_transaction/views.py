from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from phy_transaction.models import Physical
from inventory.models import Inventory, SellPrice
from product.models import Product
from counter_party.models import Counter
from django.http import HttpResponse
import simplejson as json
import logging


@login_required
def physicals(request):
    options = {}
    physicals = Physical.objects.all()
    products = Product.objects.all()
#    product_names = ''
#    for product in products:
#        product_names += product.name + ','
    counter_names = ''
    counters = Counter.objects.all()
    for counter in counters:
        counter_names += counter.name + '$'
#    inventory_names = ''
    invents = Inventory.objects.all()
#    for invent in invents:
#        inventory_names += invent.name + ','

    suppliers = Counter.objects.filter(counter_type="Supplier")
    customers = Counter.objects.filter(counter_type="Customer")
    options.update({'supplier_list': '$'.join([x.name for x in suppliers])})
    options.update({'customer_list': '$'.join([x.name for x in customers])})

    options.update({'physicals': physicals, 'counter_list': counter_names, 'product_list': products, 'invent_list':invents})
    render_to_url = 'hidden/phy_transaction.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_physical(request):
    request_vals = request.POST
    name = request_vals.get('name')
    phy_type = request_vals.get('type').strip()
    inventory_id = request_vals.get('inventory')
    product_id = request_vals.get('product')
    net_volume = request_vals.get('net_volume')
    gross_volume = request_vals.get('gross_volume')
    price = request_vals.get('price')
    counter_id = request_vals.get('counter')
    program = request_vals.get('program')
    trans_date = request_vals.get('trans_date')
    print 'trans_date=', trans_date
    print counter_id
    to_inventory = ''
    sellprice = ''
    try:
        product = Product.objects.get(name=product_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of product is incorrectly'}))
    try:
        counter = Counter.objects.get(name=counter_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of counter is incorrectly'}))
    try:
        inventory = Inventory.objects.get(name=inventory_id)
        product = Product.objects.get(name=product_id)
        sell_price = SellPrice.objects.get(inventory=inventory,product=product)
        if phy_type.lower() == 'purchase':
            print sell_price.avg_price
            if int(sell_price.avg_price) == 0:
                print '1111111111111'
                out_price = sell_price.price
            else:
                print '2222222222222222222'
                out_price = sell_price.avg_price
         
            #out_price = sell_price.price
            out_volume = sell_price.volume
            out_new_price = (out_price*out_volume + float(price)*int(gross_volume))/(out_volume + int(gross_volume))
            print '!!!!!!!!!!!!!'
            print out_price
            print out_volume
            print out_new_price
            sell_price.volume += int(gross_volume)
            sell_price.phy_volume += int(gross_volume)
            inventory.volume += int(gross_volume)
            sell_price.avg_price = out_new_price
        elif phy_type.lower() == 'sell':
#            if sell_price.volume < int(net_volume):
#                return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the product from the inventory'}))
#            else:
            out_price = sell_price.price
            out_volume = sell_price.volume
            #out_new_price = (out_price*out_volume-float(price)*int(net_volume))/(out_volume - int(net_volume))
            print '!!!!!!!!!!!!!'
            sell_price.volume -= int(gross_volume)
            inventory.volume -= int(gross_volume)
            if sell_price.phy_volume == 0:
                sell_price.phy_volume = sell_price.volume - int(gross_volume)
            else:
                sell_price.phy_volume -= int(gross_volume)
            print sell_price.volume
                #product.price = out_new_price
        elif phy_type.lower() == 'transfer':
#            if sell_price.volume < int(net_volume):
#                return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the product from the inventory'}))
#            else:
            out_volume = product.volume
                #out_new_price = (out_price*out_volume-float(price)*int(net_volume))/(out_volume - int(net_volume))
            sell_price.volume -= int(gross_volume)
            inventory.volume -= int(gross_volume)
            if sell_price.phy_volume == 0:
                sell_price.phy_volume = sell_price.volume - int(gross_volume)
            else:
                sell_price.phy_volume -= int(gross_volume)
                #product.price = out_new_price
            to_inventory = request_vals.get('to_inventory')
            if to_inventory == inventory_id:
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory and to_inventory is equivalent'}))
                
            try:
                to_invent = Inventory.objects.get(name=to_inventory)
                sellprice = SellPrice.objects.get(inventory=to_invent,product=product)
                now_volume = sellprice.volume 
                now_price = sellprice.volume
                new_volume = now_volume + int(gross_volume)
                new_price = (now_volume*now_price + int(gross_volume)* float(price))/new_volume
                sellprice.price = new_price
                sellprice.volume = new_volume
                to_invent.volume = new_volume
                if sellprice.phy_volume == 0:
                    sellprice.phy_volume = sell_price.volume + int(gross_volume)
                else:
                    sellprice.phy_volume += new_volume
                print 'AAAAAAAAAAAAAAAAAAA'
                print sellprice.price
                print sellprice.volume
                sellprice.save()
            except Exception as e:
                print e
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of to inventory  is incorrectly'}))
                
    except Inventory.DoesNotExist:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory is incorrectly'}))
         

    physical = Physical.objects.create(
        name = name,
        phy_type = phy_type,
        inventory = inventory,
        product = product,
        net_volume = net_volume,
        gross_volume = gross_volume,
        price = price,
        program = program,
        counter_party = counter,
        to_inventory = to_inventory,
        transaction_date = trans_date
    )
    physical.save()
    sell_price.save()
#    if phy_type.lower == 'transfer':
#        sell_price.save() 
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_physical(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    physicals = request_vals.getlist('physicals[]', '')
   
    Physical.objects.filter(pk__in=physicals).delete()
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_physical(request):
    request_vals = request.GET

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_physical(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    physical_id = request_vals.get('physical_id')
    name = request_vals.get('name')
    address = request_vals.get('address')
    email = request_vals.get('email')
   
    physical = Physical.objects.get(pk=physical_id)
    physical.name = name
    physical.address = address
    physical.email = email
    physical.save()
    
    
    return HttpResponse(json.dumps({'response': 'success'}))

