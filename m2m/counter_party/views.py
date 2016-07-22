from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from counter_party.models import Counter
from django.http import HttpResponse
import simplejson as json

def counters(request):
    options = {}
    counters = Counter.objects.all()
    options.update({'counters': counters})
    render_to_url = 'hidden/counter_party.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
def create_counter(request):
    request_vals = request.POST
    name = request_vals.get('name')
    address = request_vals.get('address')
    counter_type = request_vals.get('counter_type')
    identifier = request_vals.get('identifier')

    try:
        counter_party = Counter.objects.get(name=name)
        return HttpResponse(json.dumps({'response':'faliure', 'info':'The name already exists in the application'}))
    except Exception:
        pass

    counter = Counter.objects.create(
        name = name,
        address = address,
        counter_type = counter_type,
        identifier = identifier
    )
    counter.save()

    return HttpResponse(json.dumps({'response': 'success'}))
