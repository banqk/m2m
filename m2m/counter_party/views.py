from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from counter_party.models import Counter
from django.http import HttpResponse
import simplejson as json

@login_required
def counters(request):
    options = {}
    counters = Counter.objects.all()
    options.update({'counters': counters})
    render_to_url = 'hidden/counter_party.html'
    return render_to_response(render_to_url, options)

@require_http_methods(['POST'])
@csrf_exempt
@login_required
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

@require_http_methods(['POST'])
@csrf_exempt
@login_required
def update_counter(request):
    request_vals = request.POST
    counter_id = request_vals.get('counter_id')
    name = request_vals.get('name')
    counter_type = request_vals.get('counter_type')
    address = request_vals.get('address')
    try:
        counter = Counter.objects.get(name=name)
        print counter.id
        if str(counter.id) != counter_id:
            return HttpResponse(json.dumps({'response':'faliure', 'info':'The counter name already exists in the application'}))
    except Exception:
        pass

    counter = Counter.objects.get(pk=counter_id)
    counter.name = name
    counter.counter_type = counter_type
    counter.address = address
    counter.save()

    return HttpResponse(json.dumps({'response': 'success', 'info': 'Update success.'}))
@require_http_methods(['POST'])
@csrf_exempt
@login_required
def remove_counter(request):
    request_vals = request.POST
    counter_id = request_vals.get('counter_id')
    name = request_vals.get('name')
    counter_type = request_vals.get('counter_type')
    address = request_vals.get('address')
    try:
        counter = Counter.objects.get(name=name)
        print counter.id
        if str(counter.id) != counter_id:
            return HttpResponse(json.dumps({'response':'faliure', 'info':'The counter name already exists in the application'}))
    except Exception:
        pass

    counter = Counter.objects.get(pk=counter_id)
    counter.name = name
    counter.counter_type = counter_type
    counter.address = address
    counter.save()

    return HttpResponse(json.dumps({'response': 'success', 'info': 'Update success.'}))
