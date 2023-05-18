from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.models import User
# Create your views here.


class UserRegister(APIView):
    permission_classes = []
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        name = request.data.get('name')
        if not User.objects.filter(username = username):
            User.objects.create_user(
            username=username,
            password=password,
            first_name=name
            )
            return Response(
                {
                'message':'Account created'
                },
                status =  status.HTTP_200_OK
            )
        return Response(
            {
            'message':'Username already exist'
            },
            status = status.HTTP_200_OK
        )
    

class UserLogin(APIView):
    permission_classes = []

    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username = username,password = password)
        print(user)
        if user:
            token,created = Token.objects.get_or_create(user = user)
            return Response(
                {
                "message" : "Login Successful",
                "token" : token.key
                }
            )
        return Response(
            {
            "message" : "Authenticatuion Failed",
            }
        )
    

class UserLogout(APIView):
    def post(self,request):
        request.auth.delete()
        logout(request.user)
        return Response(
            {
            'message' : 'Logged out successfully',
            }
        )