from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from authenticate.serializers import  UserLoginSerializer, UserProfileSerializer, UserRegistrationSerializer, EntireUserProfileSerializer
from django.contrib.auth import authenticate
# from authenticate.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from authenticate.renderers import UserRenderer
from .models import MyUser
from django.contrib.auth.hashers import check_password
import hashlib
from django.contrib.auth.hashers import make_password

# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class UserRegistrationView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    token = get_tokens_for_user(user)
    return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.data.get('email')
    #password = request.POST['password']
    print(request.data)
    password = request.data['password']
    # password = serializer.data.get('password')
    # print(email)
    # print(password)
    # user = authenticate(email=email,password='pbkdf2_sha256$320000$RXH1iqHBi1wyQKdrWRMPzZ$GKomU6+alH3t9feLG8VsvP2UkR2x5ClOrPOGKTB3RFk=')
    # print(user)
    user = MyUser.objects.get(email=email)
    # print(user)
    # print(user.password)
    og_password = user.password
    print(password, og_password)
    # print(new_password)
    
    # print('--------------------')
    # print(og_password)
    # print(new_password)
    # print(hashlib.pbkdf2_hmac(password.encode()).hexdigest())

    #print(check_password(user.password,hashlib.sha256(password.encode())))
    # username = request.POST['email']
    # password1 = request.POST['password']



    # print(check_password(user.password,password))

    # user=authenticate(email=email,password=new_password)
    # print(user)

    # if check_password(user.password,password):

    if (check_password(password,og_password)):
      token = get_tokens_for_user(user)
      return Response({'token':token, 'msg':'Login Success','id':user.id, 'designation':user.designation}, status=status.HTTP_200_OK)
    else:
      return Response({'errors':{'non_field_errors':['Username or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

class UserProfileView(APIView):
  renderer_classes = [UserRenderer]
  #permission_classes = [IsAuthenticated]
  def get(self, request, format=None):
    serializer = UserProfileSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def EntireUserProfileView(request):
  user = request.user
  serializer = EntireUserProfileSerializer(user)
  return Response(serializer.data, status=status.HTTP_200_OK)
        