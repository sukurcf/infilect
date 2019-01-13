from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FPhoto


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response('Logged Out')

@csrf_exempt
@api_view(['GET'])
def listgroups(request):

    return Response('Hello')