from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from phy_transaction.models import Physical
from inventory.models import Inventory
from product.models import Product
from counter_party.models import Counter
from django.http import HttpResponse
import simplejson as json
import logging



def physicals(request):
    options = {}
    physicals = Physical.objects.all()
    options.update({'physicals': physicals})
    render_to_url = 'hidden/phy_transaction.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_physical(request):
    request_vals = request.POST
    name = request_vals.get('name')
    phy_type = request_vals.get('type')
    inventory_id = request_vals.get('inventory')
    product_id = request_vals.get('product')
    volume = request_vals.get('volume')
    price = request_vals.get('price')
    counter_id = request_vals.get('counter')
    print counter_id
    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory is incorrectly'}))
    try:
        product = Product.objects.get(pk=product_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of product is incorrectly'}))
    try:
        counter = Counter.objects.get(pk=counter_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of counter is incorrectly'}))
         

    physical = Physical.objects.create(
        name = name,
        phy_type = phy_type,
        inventory = inventory,
        product = product,
        volume = volume,
        price = price,
        counter_party = counter
    )
    physical.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
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

def search_physical(request):
    physical_name = request.GET.get('physical_name', '')
    physicals = Physical.objects.filter(name__icontains=physical_name)
    return HttpResponse(json.dumps({'response':physicals}))
