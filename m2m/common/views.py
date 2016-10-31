from django.shortcuts import render, render_to_response
from accounts.models import Account
from inventory.models import Inventory, SellPrice
from hedge_account.models import Hedge_Account
from users.models import User
from product.models import Product
from counter_party.models import Counter
from fuel_class.models import Fuel_Class
from hedge_instrument.models import Instrument
from hedge_transaction.models import Hedge_Tran
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import simplejson as json


def account(request):
    options = {}
    account_id = request.GET.get('account_id', '')
    fuel_type = []
    try:
        account = Account.objects.get(pk=account_id)
        if account.fuel_type is not None:
            fuel_type = [x.strip() for x in account.fuel_type.split(",") if x.strip() != ""]
        fuels = Fuel_Class.objects.filter(m2m_account=account)
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
    print products
    print fuel_type
#    options.update({'current_account_name': account.name})
    options.update({'account': account})
    options.update({'inventories': inventories})
    options.update({'hedge_accounts': hedge_accounts})
    options.update({'products': products})
    options.update({'fuels': fuels})
    options.update({'fuel_type_str': ",".join(fuel_type)})
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
    print inventory.m2m_account
    try:
        ps = json.loads(inventory.products)
    except Exception:
        ps = []
    if not isinstance(ps, list):
        ps = [ps]
    ps = [ x for x in ps if len(str(x).strip()) > 0]
    print "ps", ps
    try:
        products = Product.objects.filter(pk__in=ps)
    except Exception:
        products = []
    all_products = Product.objects.filter(m2m_account=inventory.m2m_account)
    sell_prices = SellPrice.objects.filter(inventory=inventory, product__in=products)
    print sell_prices
    ex_products = []
    ps = [int(x) for x in ps]
    in_products = []
    for e in all_products:
        if e.id not in ps:
            ex_products.append(e)
        else:
            in_products.append(e.name)
    suppliers = Counter.objects.filter(counter_type="Supplier")
    customers = Counter.objects.filter(counter_type="Customer")
    options.update({'supplier_ids': '$'.join([x.name for x in suppliers])})
    options.update({'customer_ids': '$'.join([x.name for x in customers])})
    options.update({'inventory': inventory})
    options.update({'products': products})
    options.update({'sell_prices': sell_prices})
    options.update({'product_names': ','.join(in_products)})
    options.update({'all_products': all_products})
    options.update({'ex_products': ex_products})

    invents = Inventory.objects.all()
    inventory_names = ""
    for invent in invents:
        if invent.name != inventory.name:
            inventory_names += invent.name + ','
    options.update({'to_inventory': inventory_names})

    hedge_accounts = Hedge_Account.objects.filter(m2m_account=inventory.m2m_account)
    hedge_names = ''
    for hedge in hedge_accounts:
        hedge_names += hedge.name + ','
    instrument_names = ''
    instruments = Instrument.objects.all()
    for instrument in instruments:
        instrument_names += instrument.symbol + ','

    options.update({'hedge_list': hedge_names})
    options.update({'instrument_list': instrument_names})
    render_to_url = 'hidden/edit_inventory.html'
    return render_to_response(render_to_url, options)

def hedge(request):
    options = {}
    hedge_id = request.GET.get('hedge_id', '')
    print "hedge_id ", hedge_id
    try:
        hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    except Hedge_Account.DoesNotExist:
        hedge_account = {}

    options.update({'hedge': hedge_account})
    render_to_url = 'hidden/edit_hedge_account.html'
    return render_to_response(render_to_url, options)


def hedge_tran(request):
    options = {}
    hedge_tran_id = request.GET.get('hedge_tran_id', '')
    print "hedge_tran_id ", hedge_tran_id
    try:
        hedge_tran = Hedge_Tran.objects.get(pk=hedge_tran_id)
    except Hedge_Tran.DoesNotExist:
        hedge_tran = {}

    options.update({'hedge_tran': hedge_tran})
    render_to_url = 'hidden/edit_hedge_trans.html'
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

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def get_prod(request):
    options = {}
    invent_name = request.POST.get('name')
    inventory = Inventory.objects.filter(name=invent_name)
    products = ''
    try:
        prod_ids = inventory[0].products
        if "[" in prod_ids:
            prod_ids = prod_ids[1:-1]
            prod_ids = [int(x.strip()[1:-1]) for x in prod_ids.split(',') if x.strip() != ""]
        else:
            prod_ids = [prod_ids]
        product = Product.objects.filter(pk__in=prod_ids)
    except Exception:
        product = []
    for p in product:
        products += p.name + ','
    
    options.update({'response':'success','products': products})
    return HttpResponse(json.dumps(options))
