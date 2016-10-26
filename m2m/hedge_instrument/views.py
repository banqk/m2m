from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from hedge_instrument.models import Instrument
from fuel_class.models import Fuel_Class
from counter_party.models import Counter
import simplejson as json


@login_required
def hedge_inst(request):
    options = {}
    instruments = Instrument.objects.all()
    fuels = Fuel_Class.objects.all()
    fuel_codes = ''
    for fuel in fuels:
        fuel_codes += fuel.code + ','
    counter_names = ''
    counters = Counter.objects.all()
    for counter in counters:
        counter_names += counter.name + '$'
    print '11111111111111111111'
    print counter_names
    options.update({'instruments': instruments, 'fuels':fuel_codes, 'counters':counter_names, 'months':range(1,13)})
    render_to_url = 'hidden/hedge_instrument.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def create_inst(request):
    request_vals = request.POST
    symbol = ''
    fuel_id = request_vals.get('fuel_class')
    year = request_vals.get('year')
    month = request_vals.get('month')
    expiration_date = request_vals.get('expiration_date')
    instrument = request_vals.get('instrument')
    put_call = request_vals.get('put_call')
    strike_price = request_vals.get('strike_price')
    counter_id = request_vals.get('counter_party')
    print fuel_id
    print counter_id
    print symbol
    try:
        fuel_class = Fuel_Class.objects.get(code=fuel_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of fuel_class is incorrectly'}))
    try:
        counter = Counter.objects.get(name=counter_id)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of counter party is incorrectly'}))

    inst = Instrument.objects.create(
        symbol = symbol,
        fuel_class = fuel_class,
        contract_year = year,
        contract_month = month,
        expiration_date = expiration_date,
        instrument = instrument,
        put_call = put_call,
        strike_price = strike_price,
        counter_party = counter
    )
    inst.save()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_inst(request):
    request_vals = request.POST
    hedge_accounts = request_vals.getlist('hedge_accounts[]', '')

    Hedge_Account.objects.filter(pk__in=hedge_accounts).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_inst(request):
    request_vals = request.POST
    hedge_id = request_vals.get('hedge_id')
    name = request_vals.get('name')
    institution = request_vals.get('institution')
    id_number = request_vals.get('id_number')

    hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    hedge_account.name = name
    hedge_account.institution = institution
    hedge_account.id_number = id_number
    hedge_account.save()

    return HttpResponse(json.dumps({'response': 'success'}))
