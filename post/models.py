from django.db import models

# Create your models here.
class Post(models.Model):
  writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE, verbose_name = '작성자')
  imageUrl = models.URLField(max_length = 1024, verbose_name='이미지 주소')
  content = models.TextField(verbose_name='내용')
  registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
  tags = models.ManyToManyField('tag.Tag', verbose_name='태그')

  def __str__(self):
    return self.content
  
  class Meta:
    db_table = 'djangostagram_post'
    verbose_name = '장고스타그램 포스트'
    verbose_name_plural = '장고스타그램 포스트'