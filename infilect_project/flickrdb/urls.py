from django.urls import path, re_path
from rest_framework.authtoken.views import obtain_auth_token
from .views import photoinfo
from .views import listphotoids
from .views import listgroups
from .views import Logout
from .views import listphotos

appname = 'flickrdb'

urlpatterns = [
    path('login/', obtain_auth_token, name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('groups/', listgroups, name = 'list_groups'),
    path('groups/<groupid>', listphotoids, name = 'list_photo_ids'),
    re_path('photos/$', listphotos, name = 'list_photos'),
    path('photos/<photoid>', photoinfo, name = 'photo_info'),
]
