from django.contrib import admin
from .models import Image , Video , Audio , Msg , Song , Latest , Bollywood , Hollywood , Hindiweb , Engweb , South

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'image' , 'image_created']

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' , 'video_created']

@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = [ 'id' , 'caption' , 'audio' , 'audio_created'  ]

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = [ 'id' , 'caption' , 'song' , 'song_created' ]

admin.site.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' , 'body', 'msg_created']



@admin.register(Latest)
class LatestAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' ,'latest_created']



@admin.register(Hollywood)
class HollywoodAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' ,'hollywood_created']



@admin.register(Bollywood)
class BollywoodAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' , 'bollywood_created']



@admin.register(South)
class SouthAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' , 'south_created']



@admin.register(Engweb)
class EngwebAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' , 'engweb_created']



@admin.register(Hindiweb)
class HindiwebAdmin(admin.ModelAdmin):
    list_display = ['id' , 'caption' , 'video' , 'hindiweb_created']




