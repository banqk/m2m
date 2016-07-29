from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from users.models import User
import simplejson as json
from django.core.mail import send_mail
from m2m.settings import ADMIN_EMAILS
from user_privilages.models import User_Privilage

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

    try:
        users = User.objects.get(name = user_name)
        return HttpResponse(json.dumps({'response':'failure','info': 'The username is already exists in the application.'}))
    except User.DoesNotExist:
        pass 

    role = User_Privilage.objects.get(code = 0)
    user = User.objects.create(
        name = user_name,
        password = password,
        firstName = first_name,
        lastName = last_name,
        email = email,
        user_privilages = role
    )
    user.save()
    email_address_list = []
    role = User_Privilage.objects.get(code = 1)
    try:
        admin_users = User.objects.filter(user_privilages=role)
        for admin in admin_users:
            email_address_list.append(admin.email)    
    except User.DoesNotExist:
        pass
    message = '%s has been created!' % user_name
    email_address_list.append(user.email)

    print email_address_list
    send_mail('Notifation from the M2M application', message, '847706317@qq.com',
                  email_address_list, fail_silently=False)

    return HttpResponse(json.dumps({'response': 'success'}))

@require_http_methods(['POST'])
@csrf_exempt
def update(request):
    request_vals = request.POST
    user_id = request_vals.get('user_id')
    permission = request_vals.get('permission')
    if permission.strip() == 'user':
        code = 0
    else:
        code = 1
    try:
        role = User_Privilage.objects.get(code = code)
        user = User.objects.get(pk=user_id)
        user.user_privilages = role
        user.save()
        return HttpResponse(json.dumps({'response': 'success', 'info':'Update success.'}))
    except User_Privilage.DoesNotExist:
        return HttpResponse(json.dumps({'response':'failure','info': 'The permission is not exists in the application.'}))

