from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from phy_transaction.models import Physical
from inventory.models import Inventory
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
    product_names = ''
    for product in products:
        product_names += product.name + ','
    counter_names = ''
    counters = Counter.objects.all()
    for counter in counters:
        counter_names += counter.name + '$'
    inventory_names = ''
    invents = Inventory.objects.all()
    for invent in invents:
        inventory_names += invent.name + ','

    options.update({'physicals': physicals, 'counter_list': counter_names, 'product_list': product_names, 'invent_list':inventory_names})
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
    print counter_id
    to_inventory = ''
    to_product = ''
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
        product = Product.objects.get(inventory=inventory,name=product_id)
        if phy_type.lower() == 'purchase':
            out_price = product.price
            out_volume = product.volume
            out_new_price = (out_price*out_volume-float(price)*int(net_volume))/(out_volume - int(net_volume))
            print '!!!!!!!!!!!!!'
            print out_price
            print out_volume
            print out_new_price
            product.volume -= int(net_volume)
            product.price = out_new_price
        elif phy_type.lower() == 'sell':
            if product.volume < int(net_volume):
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the product from the inventory'}))
            else:
                out_price = product.price
                out_volume = product.volume
                out_new_price = (out_price*out_volume-float(price)*int(net_volume))/(out_volume - int(net_volume))
                print '!!!!!!!!!!!!!'
                print out_price
                print out_volume
                print out_new_price
                product.volume -= int(net_volume)
                product.price = out_new_price
        elif phy_type.lower() == 'transfer':
            if product.volume < int(net_volume):
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The net volume greater than the product from the inventory'}))
            else:
                out_price = product.price
                out_volume = product.volume
                out_new_price = (out_price*out_volume-float(price)*int(net_volume))/(out_volume - int(net_volume))
                product.volume -= int(net_volume)
                product.price = out_new_price
            to_product = request_vals.get('to_product')
            to_inventory = request_vals.get('to_inventory')
            if to_inventory == inventory_id and product_id == to_product:
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of product and to_product is equivalent'}))
                
            try:
                to_invent = Inventory.objects.get(name=to_inventory)
                to_prod = Product.objects.get(inventory=to_invent,name=to_product)
                now_volume = to_prod.volumn 
                now_price = to_prod.volumn
                new_volume = now_volume + int(net_volume)
                new_price = (now_volume*now_price + int(net_volume)* float(price))/new_volume
                to_prod.price = new_price
                to_prod.volumn = new_volume
            except Exception:
                return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of to inventory or to product is incorrectly'}))
                
    except Exception:
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
        to_product = to_product
    )
    physical.save()
    product.save() 
    if phy_type.lower == 'transfer':
        to_prod.save()
    
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

