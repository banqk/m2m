from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from product.models import Product
from django.http import HttpResponse
import simplejson as json
from fuel_class.models import Fuel_Class
from accounts.models import Account
from inventory.models import Inventory
from users.models import User

@login_required
def products(request):
    options = {}
    fuel_codes = ''
    account_names = ''
    inven_names = ''
    if request.user.user_privilages.code == 1:
        fuels = Fuel_Class.objects.all()
        m2m_accounts = Account.objects.all()
        products = Product.objects.all()
        inventories = Inventory.objects.all()
    else:
        user = User.objects.filter(pk=request.user.id)
        m2m_accounts = Account.objects.filter(user = user)
        fuels = Fuel_Class.objects.filter(m2m_account__in=m2m_accounts)
        inventories = Inventory.objects.filter(m2m_account__in=m2m_accounts)
        products = Product.objects.filter(m2m_account__in=m2m_accounts)
    for fuel in fuels:
        fuel_codes += fuel.code + ','
    for account in m2m_accounts:
        account_names += account.name + ','         
    for inventory in inventories:
        inven_names += inventory.name + ','
    print fuel_codes
    print account_names
    print inven_names
    options.update({'products': products, 'fuels': fuel_codes, 'account_list': account_names, 'invent_list': inven_names})
    render_to_url = 'hidden/product.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_product(request):
    request_vals = request.POST
    name = request_vals.get('name')
    fuel_name = request_vals.get('fuel_class')
    description = request_vals.get('description')
    account_name = request_vals.get('account')
    inventory_name = request_vals.get('inventory')
    print account_name
    try:
        product = Product.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The product name already exists in the application'}))
    except Exception:
        pass

    try:
        fuel_class = Fuel_Class.objects.get(code=fuel_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of fuel class is incorrectly'}))
    try:
        account = Account.objects.get(name=account_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of m2m account is incorrectly'}))
    try:
        inventory = Inventory.objects.get(name=inventory_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of inventory is incorrectly'}))

    product = Product.objects.create(
        name = name,
        fuel_class = fuel_class,
        description = description,
        m2m_account = account,
        inventory = inventory,
    )
    product.save()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_product(request):
    request_vals = request.POST
    product_id = request_vals.get('product_id')
    name = request_vals.get('name')
    fuel_class = request_vals.get('fuel_class').strip()
    description = request_vals.get('description')
    try:
        product = Product.objects.get(name=name)
        print product.id
        if str(product.id) != product_id:
            return HttpResponse(json.dumps({'response':'faliure', 'info':'The product name already exists in the application'}))
    except Exception:
        pass
    try:
        fuel_class = Fuel_Class.objects.get(code=fuel_class)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of fuel class is incorrectly'}))

    product = Product.objects.get(pk=product_id)
    product.name = name
    product.fuel_class = fuel_class
    product.description = description
    product.save()

    return HttpResponse(json.dumps({'response': 'success', 'info': 'Update success.'}))
@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_product(request):
    request_vals = request.POST
    product_id = request_vals.get('product_id')
    name = request_vals.get('name')
    fuel_class = request_vals.get('fuel_class').strip()
    description = request_vals.get('description')
    try:
        product = Product.objects.get(name=name)
        print product.id
        if str(product.id) != product_id:
            return HttpResponse(json.dumps({'response':'faliure', 'info':'The product name already exists in the application'}))
    except Exception:
        pass
    try:
        fuel_class = Fuel_Class.objects.get(code=fuel_class)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of fuel class is incorrectly'}))

    product = Product.objects.get(pk=product_id)
    product.name = name
    product.fuel_class = fuel_class
    product.description = description
    product.save()

    return HttpResponse(json.dumps({'response': 'success', 'info': 'Update success.'}))
