from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import *
from django.contrib.auth import authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Genearte Token  Manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Create your views here.

class UserRegistrationView(APIView):

    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration successfully !'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    
    renderer_classes = [UserRenderer]

    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'token':token,'msg':'Login success'}, status=status.HTTP_200_OK)  
            else:
                return Response({'error':{'non_field_error':['Email or password field requried']}}, status=status.HTTP_404_NOT_FOUND) 


class ProfileView(APIView):
    renderer_classes = [UserRenderer]
    #permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileView(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class ChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
         return Response({'msg':'Change Password Successful'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ResetPasswordEmailView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,format=None):
        serializer = ResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Password Rest Link Send,Please check Your Email.'} , status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ResetPasswordView(APIView):
    def post(self,request,uid,token,format=None):
        serializer = UserResetPasswordSerializer(data=request.data , context = {'uid':uid , 'token':token})  
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'Reset Password Successfully'} , status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  

        


