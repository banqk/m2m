from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from hedge_transaction.models import Hedge_Tran
from hedge_account.models import Hedge_Account
from product.models import Product
from django.http import HttpResponse
import simplejson as json
import logging



def hedge_tran(request):
    options = {}
    hedge_trans = Hedge_Tran.objects.all()
    options.update({'hedge_trans': hedge_trans})
    render_to_url = 'hidden/hedge_transaction.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_hedge_tran(request):
    request_vals = request.POST
    name = request_vals.get('name')
    hedge_type = request_vals.get('type')
    hedge_id = request_vals.get('hedge_account')
    product_id = request_vals.get('product')
    volume = request_vals.get('volume')
    price = request_vals.get('price')
    initial_pos = request_vals.get('initial_pos')

    hedge_account = Hedge_Account.objects.get(pk=hedge_id)
    product = Product.objects.get(pk=product_id)

    hedge_tran = Physical.objects.create(
        name = name,
        phy_type = phy_type,
        hedge_account = hedge_account,
        product = product,
        volume = volume,
        price = price,
        initial_pos = initial_pos
    )
    hedge_tran.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))


@require_http_methods(['POST'])
@csrf_exempt
def remove_hedge_tran(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    hedge_trans = request_vals.getlist('hedge_trans[]', '')
   
    Physical.objects.filter(pk__in=hedge_trans).delete()
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_hedge_tran(request):
    request_vals = request.GET

@require_http_methods(['POST'])
@csrf_exempt
def update_hedge_tran(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    hedge_tran_id = request_vals.get('hedge_tran_id')
    name = request_vals.get('name')
    address = request_vals.get('address')
    email = request_vals.get('email')
   
    hedge_tran = Physical.objects.get(pk=hedge_tran_id)
    hedge_tran.name = name
    hedge_tran.address = address
    hedge_tran.email = email
    hedge_tran.save()
    
    
    return HttpResponse(json.dumps({'response': 'success'}))

def search_hedge_tran(request):
    hedge_tran_name = request.GET.get('hedge_tran_name', '')
    hedge_trans = Physical.objects.filter(name__icontains=hedge_tran_name)
    return HttpResponse(json.dumps({'response':hedge_trans}))
