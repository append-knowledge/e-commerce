from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .serializers import SigninSerializer,SignUpserializer,ProductSerializer,OrderSerializer
from user.models import MyUser,Order,Product
from rest_framework import generics,mixins
from rest_framework.views import APIView
from django.contrib.auth import authenticate,login
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class UserCreationView(generics.GenericAPIView,mixins.CreateModelMixin):
    model=MyUser
    serializer_class = SignUpserializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class SignInView(APIView):
    serializer_class=SigninSerializer
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'msg':'login failed'},status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(serializer.errors)


class TodoListMixin(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    model=Product
    serializer_class = Todoserialiser
    queryset = model.objects.all()
    # authentication_classes = [BasicAuthentication,SessionAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.model.objects.filter(user_name=self.request.user)

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        user=self.request.user
        print(user)
        serializer.save(user_name=user)



    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)

