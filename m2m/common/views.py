from django.shortcuts import render, render_to_response
from accounts.models import Account
from inventory.models import Inventory
from hedge_account.models import Hedge_Account


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
    
#    options.update({'current_account_name': account.name})
    options.update({'account': account})
    options.update({'inventories': inventories})
    options.update({'hedge_accounts': hedge_accounts})
    render_to_url = 'hidden/single_account.html'
    return render_to_response(render_to_url, options)

def company(request):
    options = {}
    account_id = request.GET.get('company_id', '')
    account = Account.objects.get(pk=account_id)
    render_to_url = 'hidden/single_company.html'
    return render_to_response(render_to_url, options)

def inventory(request):
    options = {}
    inventory_id = request.GET.get('inventory_id', '')
    print inventory_id

    try:
        inventory = Inventory.objects.get(pk=inventory_id)
    except Inventory.DoesNotExist:
        print '##############'
        inventory = {}
    print inventory.id
    
    options.update({'inventory': inventory})
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
