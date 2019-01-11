from django.shortcuts import render
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FPhoto


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response('Logged Out')

class ListGroups(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get(self, request, format = None):
        resp = FPhoto.objects.all().values('groupid').distinct()
        return Response(resp)