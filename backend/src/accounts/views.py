from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
User=get_user_model()


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self,request):
        try:
            data=request.data
            email = data['email']
            email=email.lower()
            name = data['name']
            last_name = data['last_name']
            password=data['password']
            re_password=data['re_password']
            is_founder = data['is_founder']
    

            if is_founder =='true':
                is_founder = True
            else:
                is_founder = False

            if password==re_password:
                if len(password)>=8:
                    if not User.objects.filter(email=email).exists():
                        if not is_founder:
                            User.objects.create_investor(email=email, name=name, last_name=last_name, password=password)
                            return Response(
                                {'success': 'investor created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                        else:
                            if is_founder:
                                User.objects.create_founder(email=email, name=name, last_name=last_name, password=password)
                                return Response(
                                {'success': 'founder created successfully'},
                                status=status.HTTP_201_CREATED
                            )
                    
                    else:
                          return Response(
                            {'error':'User with this email already exists'},
                            status=status.HTTP_400_BAD_REQUEST
                        )

                
            else:
                return Response(
                    {'error':'Password must be at least 8 characters long'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong when registering an account'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class RetrieveUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )    
