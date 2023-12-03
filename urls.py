from django.urls import path
from . import views


urlpatterns = [
    path('' , views.Dashboard , name='dashboard'),
    path('registration/',views.Registration , name='registration'),
    path('login/' , views.Login , name='login'),
    path('logout/' , views.Logout , name = 'logout'),
    path('image/' , views.Images , name = 'images'),
    path('video/' , views.Videos , name = 'videos'),
    path('audio/' , views.Audios , name = 'audios'),
    path('search/' , views.Searchimage , name = 'search'),
    path('chat/' , views.Chat , name = 'chat'),
    path('types/' , views.Types , name = 'types'),
    path('song/' , views.Songs , name = 'songs'),
    path('songtype/' , views.Songtype , name = 'songtype'),
    path('latest/' , views.Latests , name = 'latest'),
    path('hollywood/' , views.Hollywoods , name = 'hollywood'),
    path('bollywood/' , views.Bollywoods , name = 'bollywood'),
    path('south/' , views.Souths , name = 'south'),
    path('engweb/' , views.Engwebs , name = 'engweb'),
    path('hindiweb/' , views.Hindiwebs , name = 'hindiweb'),
]
