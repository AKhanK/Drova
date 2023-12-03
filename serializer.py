from app.models import Image , Video , Audio
from rest_framework import serializers

class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id' , 'caption' , 'image']

class Videoserializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields =  ['id' , 'caption' , 'video']

class Audioserializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields =  ['id' , 'caption' , 'audio']