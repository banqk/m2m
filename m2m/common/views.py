from django.shortcuts import render, render_to_response


def account(request):
    options = {}
    account_id = request.GET.get('account_id', '')
    options.update({'current_account_id': account_id})
    render_to_url = 'hidden/single_account.html'
    return render_to_response(render_to_url, options)

def company(request):
    options = {}
    account_id = request.GET.get('company_id', '')
    render_to_url = 'hidden/single_company.html'
    return render_to_response(render_to_url, options)
