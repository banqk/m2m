from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from users.models import User
import simplejson as json
from django.core.mail import send_mail

def users(request):
    options = {}
    users = User.objects.all()
    options.update({'users': users})
    render_to_url = 'hidden/users.html'
    return render_to_response(render_to_url, options)


@require_http_methods(['POST'])
@csrf_exempt
def create_user(request):
    request_vals = request.POST
    user_name = request_vals.get('name')
    password = request_vals.get('password')
    first_name = request_vals.get('first_name')
    last_name = request_vals.get('last_name')
    email = request_vals.get('email')
    print first_name
    print last_name

    try:
        users = User.objects.get(name = user_name)
        return HttpResponse(json.dumps({'response':'failure','info': 'The username is already exists in the application.'}))
    except User.DoesNotExist:
        pass 

    user = User.objects.create(
        name = user_name,
        password = password,
        firstName = first_name,
        lastName = last_name,
        email = email
    )
    user.save()
    email_address_list = []
    message = '%s has been created!' % user_name
    email_address_list.append(user.email)
    try:
        # send the email
        send_mail('Notifation from the M2M application', message, '847706317@qq.com',
                  email_address_list, fail_silently=False)
    except:
        return 'Sending email failed'

    return HttpResponse(json.dumps({'response': 'success'}))

