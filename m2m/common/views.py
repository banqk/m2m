from django.shortcuts import render, render_to_response
from accounts.models import Account
from inventory.models import Inventory
from hedge_account.models import Hedge_Account


def account(request):
    options = {}
    account_id = request.GET.get('account_id', '')
    account = Account.objects.get(pk=account_id)
    inventories = Inventory.objects.get(m2m_account=account_id)
    hedge_accounts = Hedge_Account.objects.get(m2m_account=account_id)
    options.update({'current_account_id': account_id})
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
