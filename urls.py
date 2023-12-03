from django.urls import path ,include
from app.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('imageapi' , views.Imageapi , basename = 'imageapis/'),
router.register('videoapi' , views.Videoapi , basename = 'videoapis/'),
router.register('audioapi' , views.Audioapi , basename = 'audioapis/'),


urlpatterns = [
    path('' , include(router.urls)),
    path('auth/' , include('rest_framework.urls' , namespace = 'rest_framework'))
]