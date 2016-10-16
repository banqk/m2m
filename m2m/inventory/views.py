from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from inventory.models import Inventory, SellPrice
from accounts.models import Account
from product.models import Product
from users.models import User
import simplejson as json

@login_required
def inventories(request):
    options = {}
    account_names = ''
    m2m_accounts = []
    try:
        if request.user.user_privilages.code == 1:
            inventories = Inventory.objects.all()
            m2m_accounts = Account.objects.all()
        else:
            user = User.objects.filter(pk=request.user.id)
            m2m_accounts = Account.objects.filter(user = user)
            inventories = Inventory.objects.filter(m2m_account__in=m2m_accounts)
    except Exception:
        inventories = {}

    for account in m2m_accounts:
        account_names += account.name + ','
    print account_names
    options.update({'inventories': inventories, 'inven_names':account_names})
    render_to_url = 'hidden/inventory.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_inventory(request):
    request_vals = request.POST
    name = request_vals.get('name')
    fuel_type = request_vals.get('fuel_type')
    in_location = request_vals.get('in_location')
    id_number = request_vals.get('id_number')
    account_name = request_vals.get('account_id').strip()
    volume = request_vals.get('volume').strip()
    if volume == '':
        volume = 0

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
        volumn = volume,
        m2m_account = account
    )
    inventory.save()

    return HttpResponse(json.dumps({'response': 'success', 'account_id': account.id} ))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_inventory(request):
    request_vals = request.POST
    inventories = request_vals.getlist('inventories[]', '')

    Inventory.objects.filter(pk__in=inventories).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
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

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def add_product(request):
    request_vals = request.POST
    inventory_id = request_vals.get('invent_id')
    products = request_vals.get('products', '')
    #products = request_vals.getlist('products[]', '')

    
    #if not isinstance(products, list):
    #    products = [products]
    print '************'
    print products
    products = json.loads(products)
    product_ids = []
    except_products = []
    for p in products:
        print p['id']
        product_ids.append(p['id']) 

    inventory = Inventory.objects.get(pk=inventory_id)
    try:
        ps = json.loads(inventory.products)
    except Exception:
        ps = []
    product_ids += ps
    inventory.products = json.dumps(product_ids)
    inventory.save()
    for p in products:
        product = Product.objects.get(pk=p['id'])
        try:
            sell_price = SellPrice.objects.get(inventory=inventory, product=product)
        except Exception:
            sell_price = SellPrice()

        sell_price.inventory = inventory
        sell_price.product = product
        sell_price.volume = p['volume']
        sell_price.phy_volume = p['volume']
        sell_price.price = p['price']
        sell_price.avg_price = p['price']
        sell_price.save()
    return HttpResponse(json.dumps({'response': 'success'}))

def invent_summ(request):
    #request_vals = request.POST
    #products = request_vals.getlist('products[]', '')


    #if not isinstance(products, list):
    #    products = [products]
    try:
        if request.user.user_privilages.code == 1:
            inventories = Inventory.objects.all()
            m2m_accounts = Account.objects.all()
        else:
            user = User.objects.filter(pk=request.user.id)
            m2m_accounts = Account.objects.filter(user = user)
            inventories = Inventory.objects.filter(m2m_account__in=m2m_accounts)
    except Exception:
        inventories = {}
    rows = []
    options = {}

    for inventory in inventories:
        products = inventory.products
        sell_price = SellPrice.objects.filter(inventory=inventory)
        for s in sell_price:
            new_one = s 
            rows.append(new_one)

#        sell_price.inventory = inventory
#        sell_price.product = product
#        sell_price.volume = p['volume']
#        sell_price.price = p['price']
#        sell_price.avg_price = p['price']
#        sell_price.save()
    options.update({'data': rows})
    render_to_url = 'hidden/invent_summ.html'
    return render_to_response(render_to_url, options)
