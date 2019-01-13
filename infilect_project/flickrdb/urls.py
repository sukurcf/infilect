from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import listgroups
from .views import Logout

appname = 'flickrdb'

urlpatterns = [
    path('login/', obtain_auth_token, name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('groups/', listgroups, name = 'list_groups'),
]