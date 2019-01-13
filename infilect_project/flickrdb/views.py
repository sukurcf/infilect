from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import FGroup
from .models import FPhoto
from .serializers import FPhotoSerializer


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

@csrf_exempt
@api_view(['GET'])
def listphotoids(request, groupid):
    photos = FPhoto.objects.filter(groupid=groupid).values('id')
    photos = [i['id'] for i in photos]
    photos = '\n'.join(photos)
    if not photos:
        return HttpResponse(f'No photos found with groupid - {groupid}')
    return HttpResponse(photos)

@csrf_exempt
@api_view(['GET'])
def listphotos(request):
    groupid = request.GET.get('group')
    photos = FPhoto.objects.filter(groupid=groupid)
    serializer = FPhotoSerializer(photos, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def photoinfo(request, photoid):
    photoinfo = FPhoto.objects.get(id=photoid)
    serializer = FPhotoSerializer(photoinfo, many=False)
    return Response(serializer.data)
