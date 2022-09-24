from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

from .models import *

# Create your views here.
@api_view(['POST'])
def login_view(request):
    data = request.data
    try:

        login_data = Login.objects.create(
            user = data["user"],
            passkey = data["passkey"]
        )

        login_data.save()

        return Response({"message":"user_added successfully"})
    except:
        return Response({"message":"login_info required"})