from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import Dsuser
from .forms import LoginForm

# Create your views here.

def register(request):
  if request.method == 'GET':
      return render(request, 'register.html')
  elif request.method == "POST":
      userId = request.POST.get('userId', None) # 기본값 None
      userEmail = request.POST.get('userEmail', None)
      password = request.POST.get('password', None)
      re_password = request.POST.get('re-password', None)

      res_data = {}

      if not (userId and password and re_password):
          res_data['error'] = '모든 값을 입력해야합니다.'
          return render(request, 'register.html', res_data)
      elif password != re_password:
          res_data['error'] = '비밀번호가 다릅니다.'
          return render(request, 'register.html', res_data)
      else:
        try:
          dsuser = Dsuser.objects.get(userId=userId)
        except Dsuser.DoesNotExist:
          dsuser = Dsuser(
              userId = userId,
              userEmail = userEmail,
              userPassword = make_password(password)
          )
          dsuser.save()
          print('저장됨')
          request.session['user'] = dsuser.id
          return redirect('/')
        res_data['error'] = '이미 등록된 아이디입니다.'
        return render(request, 'register.html', res_data)

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      request.session['user'] = form.user_id
      # session코드
      return redirect('/')
  else:
      form = LoginForm()
  return render(request, 'login.html', {'form' : form})

def logout(request):
  if request.session.get('user'):
      del(request.session['user'])

  return redirect('/')