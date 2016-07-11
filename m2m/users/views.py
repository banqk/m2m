from django.shortcuts import render, render_to_response
from users.models import User

def users(request):
    options = {}
    users = User.objects.all()
    options.update({'users': users})
    render_to_url = 'hidden/users.html'
    return render_to_response(render_to_url, options)


@require_http_methods(['POST'])
@csrf_exempt
def create_account(request):
    request_vals = request.POST
    logger = logging.getLogger('')
    logger.info(str(request))
    user_name = request_vals.get('name')
    password = request_vals.get('password')
    first_name = request_vals.get('first_name')
    last_name = requet_vals.get('last_name')
    email = request_vals.get('email')

    user = User.objects.create(
        name = user_name,
        password = password,
        first_name = first_name,
        last_name = last_name,
        email = email
    )
    user.save()

    return HttpResponse(json.dumps({'response': 'success'}))

