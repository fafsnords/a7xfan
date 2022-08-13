from django.shortcuts import redirect, render
from django.http import JsonResponse
from . models import Data
from . models import POST

def index(request):
    return render(request, 'web/index.html')

def sign_up(request):
    if request.method == 'POST':
      Username = request.POST['user']
      Email = request.POST['mail']
      Password = request.POST['pass']
      if not Data.objects.all().filter(username = Username):
        User = request.session['user'] = Username
        Pass = request.session['pass'] = Password
        Data(username = User, email = Email, password = Pass).save()
        return redirect('/forum')
      else:
        return render(request, 'web/register.html', {'alert':'<script>alert("username already taken");</script>'})
    else:
      return render(request, 'web/register.html')

def sign_in(request):
    if request.method == 'POST':
      Username = request.POST['user']
      Password = request.POST['pass']
      if Data.objects.all().filter(username = Username, password = Password):
        request.session['user'] = Username
        request.session['pass'] = Password
        return redirect('/forum')
      else:
        return render(request, 'web/login.html', {'alert':'<script>alert("incorrect username or password try again");</script>'})
    else:
      return render(request, 'web/login.html')

def forum(request):
    if request.session.get('user') and request.session.get('pass'):
      for data in str(Data.objects.all().count()):
         convert = {}
         if request.method == 'POST':
           Post = request.POST.get('post')
           convert['post'] = Post
           convert['username'] = request.session.get('user')
           POST(username = request.session.get('user'), post = Post).save()
           return JsonResponse(convert)
         return render(request, 'web/forum.html', {'total':data, 'Data':POST.objects.all().values()})
    else:
      return redirect('/sign_in')

def log_out(request):
    try:
       del request.session['user']
       del request.session['pass']
    except:
       pass
    return redirect('/sign_in')