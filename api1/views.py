from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . serializers import Myserializer
from . models import Mytable

@api_view(['GET'])
def get_users(request):
    users = Mytable.objects.all()
    cup = Myserializer(users, many=True) 
    return Response(cup.data)

@api_view(['POST'])
def create_user(request):
    cup = Myserializer(data=request.data)

    if cup.is_valid():
        cup.save()
        return Response(cup.data, status=status.HTTP_201_CREATED)
    return Response(cup.errors, status=status.HTTP_400_BAD_REQUEST)