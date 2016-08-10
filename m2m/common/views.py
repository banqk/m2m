from django.shortcuts import render, render_to_response
from accounts.models import Account
from inventory.models import Inventory
from hedge_account.models import Hedge_Account
from users.models import User
from product.models import Product
from counter_party.models import Counter
from fuel_class.models import Fuel_Class
from django.contrib.auth.decorators import login_required
import json


def account(request):
    options = {}
    account_id = request.GET.get('account_id', '')

    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        pass
    try:
        inventories = Inventory.objects.filter(m2m_account=account_id)
    except Inventory.DoesNotExist:
        inventories = {}
    try:
        hedge_accounts = Hedge_Account.objects.filter(m2m_account=account_id)
    except Hedge_Account.DoesNotExist:
        hedge_accounts = {}
    products = Product.objects.filter(m2m_account=account_id)
#    options.update({'current_account_name': account.name})
    options.update({'account': account})
    options.update({'inventories': inventories})
    options.update({'hedge_accounts': hedge_accounts})
    options.update({'products': products})
    render_to_url = 'hidden/single_account.html'
    return render_to_response(render_to_url, options)
def user(request):
    options = {}
    user_id = request.GET.get('user_id', '')

    try:
        user = User.objects.get(pk=user_id)
    except Account.DoesNotExist:
        pass
    
#    options.update({'current_account_name': account.name})
    options.update({'user': user})
    render_to_url = 'hidden/single_user.html'
    return render_to_response(render_to_url, options)

def company(request):
    options = {}
    account_id = request.GET.get('company_id', '')
    account = Account.objects.get(pk=account_id)
    render_to_url = 'hidden/single_company.html'
    return render_to_response(render_to_url, options)

@login_required
def inventory(request):
    options = {}
    inventory_id = request.GET.get('inventory_id', '')
    print inventory_id

    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except Inventory.DoesNotExist:
        inventory = {}
#    try:
    print inventory.m2m_account
    try:
        ps = json.loads(inventory.products)
    except Exception:
        ps = []
    products = Product.objects.filter(pk__in=ps)
#    except Product.DoesNotExist:
#        products = {}
    e_products = Product.objects.filter(m2m_account = inventory.m2m_account)
    ex_products = []
    ps = [int(x) for x in ps]
    for e in e_products:
        if e.id not in ps:
            print e.id
            print e.name
            ex_products.append(e) 
    options.update({'inventory': inventory})
    options.update({'products': products})
    options.update({'ex_products': ex_products})
    render_to_url = 'hidden/edit_inventory.html'
    return render_to_response(render_to_url, options)

def hedge(request):
    options = {}
    hedge_id = request.GET.get('hedge_id', '')

    try:
        hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    except Hedge_Account.DoesNotExist:
        hedge_account = {}
    
    options.update({'hedge': hedge_account})
    render_to_url = 'hidden/edit_hedge_account.html'
    return render_to_response(render_to_url, options)
def product(request):
    options = {}
    product_id = request.GET.get('product_id', '')

    try:
        product = Product.objects.get(pk=product_id)
    except Hedge_Account.DoesNotExist:
        product = {}
    
    options.update({'product': product})
    render_to_url = 'hidden/edit_product.html'
    return render_to_response(render_to_url, options)
def counter(request):
    options = {}
    counter_id = request.GET.get('counter_id', '')

    try:
        counter = Counter.objects.get(pk=counter_id)
    except Hedge_Account.DoesNotExist:
        counter = {}
    
    options.update({'counter': counter})
    render_to_url = 'hidden/edit_counter.html'
    return render_to_response(render_to_url, options)
def instrument(request):
    options = {}
    hedge_id = request.GET.get('hedge_id', '')

    try:
        hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    except Hedge_Account.DoesNotExist:
        hedge_account = {}
    
    options.update({'hedge': hedge_account})
    render_to_url = 'hidden/edit_hedge_account.html'
    return render_to_response(render_to_url, options)
def fuel_class(request):
    options = {}
    fuel_id = request.GET.get('fuel_id', '')

    try:
        fuel = Fuel_Class.objects.get(pk=fuel_id)
    except Fuel_Class.DoesNotExist:
        fuel = {}
    
    options.update({'fuel': fuel})
    render_to_url = 'hidden/edit_fuel.html'
    return render_to_response(render_to_url, options)
