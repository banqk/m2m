from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from fuel_class.models import Fuel_Class
from inventory.models import Inventory
from accounts.models import Account
from users.models import User
import simplejson as json
from django.http import HttpResponse,HttpResponseRedirect


@login_required
def fuels(request):
    options = {}
    try:
        if request.user.user_privilages.code == 1:
            fuels = Fuel_Class.objects.all()
            m2m_accounts = Account.objects.all()
        else:
            user = User.objects.filter(pk=request.user.id)
            m2m_accounts = Account.objects.filter(user = user)
            fuels = Fuel_Class.objects.filter(m2m_account__in=m2m_accounts)
    except Exception:
        fuels = {}
    options.update({'fuel_classes': fuels, 'account_list': m2m_accounts})
    render_to_url = 'hidden/fuel_class.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_fuel(request):
    request_vals = request.POST
    code = request_vals.get('code')
    description = request_vals.get('description')
    account_name = request_vals.get('account_name')
    print account_name

    try:
        fuel = Fuel_Class.objects.get(code=code)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The code already exists in the application'}))
    except Exception:
        pass
    try:
        account = Account.objects.get(name=account_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of m2m account is incorrectly'}))

    fuel = Fuel_Class.objects.create(
        code = code,
        description = description,
        m2m_account = account,
    )
    fuel.save()

    return HttpResponse(json.dumps({'response': 'success'} ))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_fuel(request):
    request_vals = request.POST
    inventories = request_vals.getlist('inventories[]', '')

    Inventory.objects.filter(pk__in=inventories).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_fuel(request):
    request_vals = request.POST
    fuel_id = request_vals.get('fuel_id')
    code = request_vals.get('code').strip()
    description = request_vals.get('description')

    try:
        fuel = Fuel_Class.objects.get(code=code)
        print fuel.id
        if str(fuel.id) != fuel_id:
            return HttpResponse(json.dumps({'response':'faliure', 'info':'The fuel class code already exists in the application'}))
    except Exception:
        pass

    fuel = Fuel_Class.objects.get(pk=fuel_id)
    fuel.code = code
    fuel.description = description
    fuel.save()

    return HttpResponse(json.dumps({'response': 'success', 'info':'Update success'}))
