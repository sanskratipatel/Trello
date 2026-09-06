from django.shortcuts import render
from rest_framework.permissions import AllowAny 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework import generics
from .serializers import SignupSerializer , LoginSerializer, ForgotPasswordSerializer , LogoutSerializer
# Create your views here.


class SignupView(generics.CreateAPIView) : 
    serializer_class = SignupSerializer 
    permission_classes = [AllowAny] 
    def create(self,request,*args , **kwargs) : 
        serializer = self.get_serializer( 
            data =request.data
        ) 
        serializer.is_valid(raise_exception=True) 
        user = serializer.save() 
        return Response( 
            { 
                "message" : "User Created Successfully" , 
                
            },
            status = status.HTTP_200_OK
        )

class LoginView(generics.GenericAPIView) : 
    serializer_class = LoginSerializer 
    permission_classes = [AllowAny] 
    def post(self , request) : 
        serializer =self.get_serializer( 
            data =request.data
        ) 
        serializer.is_valid( 
            raise_exception=True
        ) 
        user = serializer.validated_data["user"] 
        refresh =RefreshToken.for_user(user)  
        refresh["name"] = user.name 
        refresh["email"] = user.email 
        refresh["role"] = user.role.name 
        access_token = refresh.access_token
        return Response(  
            {
            "message": "Login Sucessful" , 
            "access" : str(access_token) , 
            "refresh" :str(refresh) 
            }, 
            status=status.HTTP_200_OK
        )


class ForgotPasswordView(generics.GenericAPIView):

    serializer_class = ForgotPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Password reset link generated successfully."
            },
            status=status.HTTP_200_OK
        )

class LogoutView(generics.GenericAPIView):

    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            {
                "message": "Logout successful"
            },
            status=status.HTTP_200_OK
        )