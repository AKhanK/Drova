from django.shortcuts import render , redirect 
from .forms import Register_form , Login_form
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from app.models import Image , Video , Audio , Msg , Song , Latest , Hollywood , Bollywood , South , Engweb , Hindiweb 
from .forms import ImageForm , Video_form , Audio_form , MsgForm , Song_form , Lastest_form , Hollywood_form , Bollywood_form , South_form , Engweb_form , Hindiweb_form
from datetime import datetime
from django.core.paginator import Paginator , PageNotAnInteger




def Registration(request):
        form = Register_form()
        if request.method == "POST":
             form = Register_form(request.POST)
             if form.is_valid():
                  form.save()
                  return redirect('login')
        
        return render(request , 'authentication/registration.html', {'register_form':form})





def Login(request):
       form = Login_form()
       if request.method == "POST":
             form = Login_form(request , (request.POST))
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request , username=username , password=password)

             if user is not None:
                auth.login(request , user)
            
                return redirect('dashboard')


       return render(request , 'authentication/login.html' , {'login_form': form})





def Dashboard(request):
     d = datetime.now()

     return render(request , "management/dashboard.html",{'dt':d} )




@login_required(login_url='login')
def Images(request ):
      img=Image.objects.all()
      if request.method == "POST":
           form=ImageForm(data=request.POST,files=request.FILES)
           if form.is_valid():
              form.save()
              obj=form.instance
              return render(request,"management/images.html" , {'obj':obj })
      else:
             form = ImageForm()
             img=Image.objects.all().order_by('-image_created')
             paginator = Paginator(img , 6)
             page = request.GET.get('page')
             img = paginator.get_page(page)
             total_pages = img.paginator.num_pages
             try:
               img=paginator.page(page)
             except PageNotAnInteger:
               img=paginator.page(1)
             except:
               img=paginator.page(paginator.num_pages)
      return render(request,"management/images.html",{"img":img, "form":form  ,'page':page ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})
          
     



@login_required(login_url='login')
def Videos(request):
    all_video=Video.objects.all().order_by('-video_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Video_form()
    return render(request,'management/videos.html',{"form":form,"all":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})




@login_required(login_url='login')
def Audios(request):
    all_audio=Audio.objects.all().order_by('caption')
    paginator = Paginator(all_audio , 5)
    page = request.GET.get('page')
    all_audio = paginator.get_page(page)
    total_pages = all_audio.paginator.num_pages
    
    try:
        all_audio=paginator.page(page)
    except PageNotAnInteger:
        all_audio=paginator.page(1)
    except:
        all_audio=paginator.page(paginator.num_pages)

    if request.method == "POST":
        form=Audio_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('audios')
    else:
         form=Audio_form()
    return render(request,'management/audios.html',{"form":form,"allo":all_audio , 'page':page  , 'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})



@login_required(login_url='login')
def Searchimage(request):
    query = request.GET['query']
    img = Image.objects.filter(caption__icontains=query)
    all = Video.objects.filter(caption__icontains=query)
    alloo = Song.objects.filter(caption__icontains=query)
    allo = Audio.objects.filter(caption__icontains=query)
    a = Hollywood.objects.filter(caption__icontains=query)
    aa = Bollywood.objects.filter(caption__icontains=query)
    aaa = Latest.objects.filter(caption__icontains=query)
    b = South.objects.filter(caption__icontains=query)
    bb = Engweb.objects.filter(caption__icontains=query)
    bbb = Hindiweb.objects.filter(caption__icontains=query)
    context ={
        'img': img ,
        'all' : all,
        'allo' : allo,
        'al' : alloo,
        'a' : a , 
        'aa' : aa , 
        'aaa' : aaa ,
        'b' : b ,
        'bb' : bb ,
        'bbb' : bbb
       
    }
    return render(request , 'management/search.html' , context )




@login_required(login_url='login')
def Chat(request):
     if request.user.is_authenticated: 
       form = MsgForm(request.POST or None )
       if request.method == 'POST':
           if form.is_valid():
               msg = form.save(commit=False)
               msg.user = request.user
               msg.save()
              # messages.success(request ,("Posted!"))
               return redirect('chat')
       msgs = Msg.objects.all().order_by("-msg_created")
       return render(request , 'management/chat.html' ,{'msgs':msgs , 'form':form})
       
     msgs = Msg.objects.all().order_by("-msg_created")
     return render(request , 'management/chat.html' ,{'msgs':msgs})


def Types(request):
    return render(request , 'management/types.html')


def Songtype(request):
    return render(request , 'management/songtype.html')


@login_required(login_url='login')
def Songs(request):
    all_video=Song.objects.all().order_by('-song_created')
    paginator = Paginator(all_video , 2)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Song_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('songs')
    else:
         form=Video_form()
    return render(request,'management/songs.html',{"form":form,"al":all_video , 'page':page  , 'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})




def Logout(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def Latests(request):
    all_video=Latest.objects.all().order_by('-latest_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Lastest_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Lastest_form()
    return render(request,'movies/latest.html',{"form":form,"aaa":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})


@login_required(login_url='login')
def Hollywoods(request):
    all_video=Hollywood.objects.all().order_by('caption')
    paginator = Paginator(all_video , 2)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Hollywood_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Hollywood_form()
    return render(request,'movies/hollywood.html',{"form":form,"a":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})



@login_required(login_url='login')
def Bollywoods(request):
    all_video=Bollywood.objects.all().order_by('-bollywood_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Bollywood_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Bollywood_form()
    return render(request,'movies/bollywood.html',{"form":form,"aa":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})



@login_required(login_url='login')
def Souths(request):
    all_video=South.objects.all().order_by('-south_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=South_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=South_form()
    return render(request,'movies/south.html',{"form":form,"b":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})



@login_required(login_url='login')
def Engwebs(request):
    all_video=Engweb.objects.all().order_by('-engweb_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Engweb_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Engweb_form()
    return render(request,'movies/engweb.html',{"form":form,"bb":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})



@login_required(login_url='login')
def Hindiwebs(request):
    all_video=Hindiweb.objects.all().order_by('-hindiweb_created')
    paginator = Paginator(all_video , 5)
    page = request.GET.get('page')
    all_video = paginator.get_page(page)
    total_pages = all_video.paginator.num_pages
    
    try:
        all_video=paginator.page(page)
    except PageNotAnInteger:
        all_video=paginator.page(1)
    except:
        all_video=paginator.page(paginator.num_pages)
    if request.method == "POST":
        form=Hindiweb_form(data=request.POST,files=request.FILES)
        if form.is_valid():
           form.save()
           return redirect ('videos')
    else:
         form=Hindiweb_form()
    return render(request,'movies/hindiweb.html',{"form":form,"bbb":all_video ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})




        
        






        
  









"""@login_required(login_url='login')
def Images(request ):
      all_video=Image.objects.all()
      paginator = Paginator(all_video , 6)
      page = request.GET.get('page')
      all_video = paginator.get_page(page)
      total_pages = all_video.paginator.num_pages
      try:
        all_video=paginator.page(page)
      except PageNotAnInteger:
        all_video=paginator.page(1)
      except:
        all_video=paginator.page(paginator.num_pages)
      if request.method == "POST":
           form=ImageForm(data=request.POST,files=request.FILES)
           if form.is_valid():
              form.save()
              obj=form.instance
              return render(request,"management/images.html" , {'obj':obj })
           else:
             form = ImageForm()
             img=Image.objects.all()
             return render(request,"management/images.html",{"img":img, "form":form ,'aa':all_video ,'page':page ,'last':total_pages , 'page_list':[i+1 for i in range(total_pages)]})
          
      return render(request , 'management/images.html')"""