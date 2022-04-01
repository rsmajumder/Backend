
from urllib import response
from rest_framework.response import Response
from rest_framework import generics, permissions
from knox.models import AuthToken
from .serializers import UserSerializer,RegisterSerializer,userProfileSerializer,OTPSerializer,OTPCheckserializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User,auth
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated 
from django.http import HttpResponse
from .models import *
from random import randint
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
          
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

        

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    @csrf_exempt
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        __, token = AuthToken.objects.create(user)
        login(request, user)

        return Response({
            'user' : {
                'id' : user.id,
                'username' : user.username,
                'phone' : user.phone,
                'first_name' : user.first_name,
                'last_name' : user.last_name,
            },
            'token' : token
        })
        
        # response = User.objects.filter(username = user).values()
        # temp_list=super(LoginAPI, self).post(request, format=None)
        # print(token)
        # print(temp_list)
        # {"data":temp_list.data}}
        # return Response(response)
        # return super(LoginAPI, self).post(request, format=None)
      

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    @csrf_exempt
    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    @csrf_exempt
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserProfileAPI(generics.GenericAPIView):
    serializer_class = userProfileSerializer

    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if serializer.is_valid():
            userprofile=serializer.save()
        return HttpResponse("<h1> OK </h1>")


class OTPLogin(generics.GenericAPIView):
    serializer_class = OTPSerializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            number = request.data.get('number')
            try:
                user = User.objects.get(phone=number)
                x=OTP(number=number,otp=''.join(["{}".format(randint(0, 9)) for num in range(0,6)]) )
                x.save()
                request.session['phone'] = number
                return HttpResponseRedirect('otpcheck/')
            except User.DoesNotExist:
                print("Enter Proper Phone Number.")
        
        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

        return Response(response)
    

class OTPCheck(generics.GenericAPIView):
    serializer_class = OTPCheckserializer
    @csrf_exempt
    def post(self,request,*args,**kwargs):
        number=request.session['phone']
        otp=request.data.get('otp')
        try:
            otp_verified=OTP.objects.get(number=number)
            if(otp_verified.otp==otp):
                print("OK")
                user=User.objects.get(phone=number)
                auth.login(request,user)
            else:
                print("Not Ok")
            
        except Exception as e:
            print(e)
        
        otp_verified.delete()

        response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
        return Response(response)


    