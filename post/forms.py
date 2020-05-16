from django import forms

class PostForm(forms.Form):
  imageUrl = forms.URLField(
    error_messages={
      'required' : '이미지 주소를 입력해주세요'
    }, label='이미지 주소'
  )
  content = forms.CharField(
    error_messages={
      'required' : '내용을 입력해주세요.'
    },
    widget=forms.Textarea, label='내용'
  )
  tags = forms.CharField(
    required=False, label='태그')
