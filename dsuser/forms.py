from django import forms
from .models import Dsuser
from django.contrib.auth.hashers import check_password

class LoginForm(forms.Form):
  userId = forms.CharField(max_length=32, label='아이디', error_messages={'required' : '아이디를 입력해주세요..'})
  userPassword = forms.CharField(widget=forms.PasswordInput, label='비밀번호', error_messages={'required' : '비밀번호를 입력해주세요..'})

  def clean(self):
    cleaned_data = super().clean()
    userId = cleaned_data.get('userId')
    userPassword = cleaned_data.get('userPassword')

    if userId and userPassword:
      try:
        dsuser = Dsuser.objects.get(userId=userId)
      except Dsuser.DoesNotExist:
        self.add_error('userId', '아이디가 없습니다')
        return
      if not check_password(userPassword, dsuser.userPassword):
        self.add_error('userPassword', '비밀번호가 틀렸습니다')
      else:
        self.user_id = dsuser.id