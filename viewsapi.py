from .serializer import Imageserializer , Videoserializer , Audioserializer
from app.models import Image , Video , Audio
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination 


class Imageapi(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = Imageserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [PageNumberPagination]
    filter_backends = [SearchFilter]
    search_fields = ['caption']

class Videoapi(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = Videoserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [PageNumberPagination]
    filter_backends = [SearchFilter]
    search_fields = ['caption']

class Audioapi(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = Audioserializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [PageNumberPagination]
    filter_backends = [SearchFilter]
    search_fields = ['caption']