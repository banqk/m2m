from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from fuel_class.models import Fuel_Class
from accounts.models import Account
import simplejson as json


def fuels(request):
    options = {}
    fuels = Fuel_Class.objects.all()
    options.update({'fuel_classes': fuels})
    render_to_url = 'hidden/fuel_class.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_fuel(request):
    request_vals = request.POST
    code = request_vals.get('code')
    description = request_vals.get('description')

    try:
        fuel = Fuel_Class.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The code already exists in the application'}))
    except Exception:
        pass

    fuel = Fuel_Class.objects.create(
        code = code,
        description = description,
    )
    fuel.save()

    return HttpResponse(json.dumps({'response': 'success'} ))

@require_http_methods(['POST'])
@csrf_exempt
def remove_fuel(request):
    request_vals = request.POST
    inventories = request_vals.getlist('inventories[]', '')

    Inventory.objects.filter(pk__in=inventories).delete()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
def update_fuel(request):
    request_vals = request.POST
    fuel_id = request_vals.get('fuel_id')
    name = request_vals.get('name')
    fuel_type = request_vals.get('fuel_type')
    location = request_vals.get('in_location')
    id_number = request_vals.get('id_number')
    volumn = request_vals.get('volumn')

    fuel = Inventory.objects.get(pk=fuel_id)
    fuel.name = name
    fuel.fuel_type = fuel_type
    fuel.location = location
    fuel.id_number = id_number
    fuel.volumn = volumn
    fuel.save()

    return HttpResponse(json.dumps({'response': 'success'}))
