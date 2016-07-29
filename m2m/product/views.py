from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from django.http import HttpResponse
import simplejson as json
from fuel_class.models import Fuel_Class

def products(request):
    options = {}
    products = Product.objects.all()
    fuels = Fuel_Class.objects.all()
    fuel_codes = ''
    for fuel in fuels:
        fuel_codes += fuel.code + ','
    print fuel_codes
    options.update({'products': products, 'fuels': fuel_codes})
    render_to_url = 'hidden/product.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_product(request):
    request_vals = request.POST
    name = request_vals.get('name')
    fuel_name = request_vals.get('fuel_class')
    description = request_vals.get('description')
    try:
        product = Product.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The product name already exists in the application'}))
    except Exception:
        pass

    try:
        fuel_class = Fuel_Class.objects.get(code=fuel_name)
    except Exception:
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The value of fuel class is incorrectly'}))

    product = Product.objects.create(
        name = name,
        fuel_class = fuel_class,
        description = description,
    )
    product.save()

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
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
