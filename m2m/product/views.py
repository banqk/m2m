from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from product.models import Product
from django.http import HttpResponse
import simplejson as json

def products(request):
    options = {}
    products = Product.objects.all()
    options.update({'products': products})
    render_to_url = 'hidden/product.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_product(request):
    request_vals = request.POST
    name = request_vals.get('name')
    fuel_class = request_vals.get('fuel_class')

    product = Product.objects.create(
        name = name,
        fuel_class = fuel_class,
    )
    product.save()

    return HttpResponse(json.dumps({'response': 'success'}))
