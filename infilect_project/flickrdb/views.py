from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FGroup
from .models import FPhoto


class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response('Logged Out')

@csrf_exempt
@api_view(['GET'])
def listgroups(request):
    groups = FGroup.objects.all()
    groups = [', '.join([i.groupname, i.id, str(i.noofphotos)]) for i in groups]
    groups = '\n'.join(groups)
    first_row = 'Groupname, Groupid, No.of photos\n'
    return HttpResponse(first_row+groups)

