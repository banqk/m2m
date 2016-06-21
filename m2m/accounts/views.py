from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import logging


def index(request):
    render_to_url = 'value/value.html'
    return render_to_response(render_to_url)

def accounts(request):
    render_to_url = 'hidden/account.html'
    return render_to_response(render_to_url)
def log(request):
    render_to_url = 'transactions_log.html'
    return render_to_response(render_to_url)

@require_http_methods(['POST'])
@csrf_exempt
def create_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    user_name = request_vals.get('user_name')
    print user_name
    password = request.POST.get('password')
    
    render_to_url = 'hidden/account.html'
    return render_to_response(render_to_url)
# Create your views here.
