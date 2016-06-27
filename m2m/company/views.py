from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from company.models import Company
import simplejson as json

def companies(request):
    options = {}
    companies = Company.objects.all()
    options.update({'companies': companies})
    render_to_url = 'hidden/company.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_company(request):
    request_vals = request.POST
    company_name = request_vals.get('company_name')
    address = request_vals.get('address')
    
    company = Company.objects.create(
        name = company_name,
        address = address
    )
    
    company.save()
    
    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
def remove_company(request):
    request_vals = request.POST
    companies = request_vals.getlist('companies[]', '')
    
    Company.objects.filter(pk__in=companies).delete()
   
    return HttpResponse(json.dumps({'response': 'success'}))
