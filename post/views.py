from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from dsuser.models import Dsuser
from tag.models import Tag
from .forms import PostForm
from .models import Post
from django.http import Http404


# Create your views here.
def index(request):
  # all_boards = Board.objects.all().order_by('-id') # - : 역순
  all_posts = Post.objects.all().order_by('-id')
  page = int(request.GET.get('p', 1)) # 없으면 1 페이지
  paginator = Paginator(all_posts, 4) # 한페이지 2개씩 나오게 설정

  posts = paginator.get_page(page)
  if not request.session.get('user'):
    return render(request, 'timeline.html', {'posts' : posts})
  else:
    return render(request, 'timeline.html', {'posts' : posts, 'userId' : Dsuser.objects.get(pk=request.session.get('user')).userId})

def post_upload(request):
    if not request.session.get('user'):
        return redirect('/user/login')
    if request.method == 'POST':
      form = PostForm(request.POST)
      if form.is_valid():
          user_id = request.session.get('user')
          dsuser = Dsuser.objects.get(pk=user_id)
          tags = form.cleaned_data['tags'].split(',')

          post = Post()
          post.imageUrl = form.cleaned_data['imageUrl']
          post.content = form.cleaned_data['content']
          post.writer = dsuser
          post.save()

          for tag in tags:
            if not tag:
              continue
            # _tag, created = Tag.objects.get_or_create(name=tag) #name=tag 조건 일치하는게 있으면 가져오고 없으면 생성한다 #writer=writer : 작성자도 같은 사람 #_tag 에는 가져오거나 생성한 객체 반환, created에는 생성한건지 아닌지 여부
            _tag, _ = Tag.objects.get_or_create(name=tag.lstrip()) #두번째 반환값 필요없어서 underbar 처리(python 문법) #lstrip : 왼쪽 공백 제거
            post.tags.add(_tag)

          return redirect('/')
    else:
      form = PostForm()
    return render(request, 'post_upload.html', {'form' : form})

def post_detail(request, pk):
  try:
    post = Post.objects.get(pk=pk)
  except Post.DoesNotExist:
      raise Http404('게시글을 찾을 수 없습니다')
  return render(request, 'post_detail.html', {'post' : post})