from django.shortcuts import render
import random
import re
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import CustomUser
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout


# Create your views here.

def generate_session_tokens(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]) for _ in range(length))


@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error':'Send a post request with valid parameters only'})

    username = request.POST['email']
    password = request.POST['password']

    # validation part

    if not re.match("[\w\d.+]+@[\w\d]+(?:\.[a-z]{2,4}){1,2}",username):
        return JsonResponse({'error':'Enter a valid email'})

    if len(password) < 8:
        return JsonResponse({'error':'Enter a valid password'})

    Usermodel = get_user_model()


    try:
        
        user = Usermodel.objects.get(email = username)
        if user.check_password(password):
            user_dict = Usermodel.objects.filter(email=username).values().first()
            user_dict.pop('password')

            if user.session_token !="0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'Previous session exists'})

            token = generate_session_tokens()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token':token , 'user': user_dict})

        else:
            return JsonResponse({'error':'Invlid password'})


    except Usermodel.DoesNotExist:
        return JsonResponse({'error':'Invalid Email'})

def signout(request, id):
    logout(request)

    Usermodel = get_user_model()

    try:
        user = Usermodel.objects.get(pk=id)
        user.session_token = "0"
        user.save()
        
    except Usermodel.DoesNotExist:
        return JsonResponse({'error':'Invalid user ID'})

    return JsonResponse({'success':'Logout Successfully'})

class UserViewset(viewsets.ModelViewSet):
    permission_classes_by_action ={'create':[AllowAny]}

    queryset = CustomUser.objects.all().order_by('id') 
    serializer_class = UserSerializer


    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return[permission() for permission in self.permission_classes]