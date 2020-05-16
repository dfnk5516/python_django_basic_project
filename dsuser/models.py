from django.db import models

# Create your models here.
class Dsuser(models.Model):
  objects = models.Manager()
  userId = models.CharField(max_length=32, verbose_name='아이디')
  userEmail = models.EmailField(max_length=128, verbose_name='이메일')
  userPassword = models.CharField(max_length=64, verbose_name='비밀번호')
  registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

  def __str__(self):
    return self.userId

  class Meta:
    db_table = 'djangostagram_dsuser'
    verbose_name = '장고스타그램 사용자'
    verbose_name_plural = '장고스타그램 사용자'