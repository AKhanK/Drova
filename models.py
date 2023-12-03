from django.db import models
from .validators import file_size
from django.contrib.auth.models import User


class Msg(models.Model):
    user = models.ForeignKey(User , related_name='msg' ,  on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=30)
    msg_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return(
            f"{self.user}"
            f" - {self.msg_created:%Y-%m-%d %H:%M} - : "
            f"{self.body}..."
            )


class Image(models.Model):
      caption=models.CharField(max_length=100)
      image=models.ImageField(upload_to="img/%y")
      image_created = models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
         return self.caption




class Video(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True)
      video_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      

class Audio(models.Model):
      caption=models.CharField(max_length=100)
      audio=models.FileField(upload_to="video/%y",validators=[file_size])
      audio_created = models.DateTimeField(auto_now_add=True)

      def __str__(self):
       return self.caption
      



class Song(models.Model):
      caption=models.CharField(max_length=100)
      song=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True) 
      song_created = models.DateTimeField(auto_now_add=True)


      def __str__(self):
         return self.caption
      

class Latest(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True) 
      latest_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      

class Hollywood(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      hollywood_created = models.DateTimeField(auto_now_add=True)
      thumb = models.FileField(upload_to="thumb/%y" , blank = True)


      def __str__(self):
         return self.caption
      

class Bollywood(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True) 
      bollywood_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      

class South(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True)
      south_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      

class Engweb(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True) 
      engweb_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      

class Hindiweb(models.Model):
      caption=models.CharField(max_length=100)
      video=models.FileField(upload_to="video/%y",validators=[file_size])
      thumb = models.FileField(upload_to="thumb/%y" , blank = True) 
      hindiweb_created = models.DateTimeField(auto_now_add=True)



      def __str__(self):
         return self.caption
      





      

