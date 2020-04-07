from django.http import Http404, HttpResponseRedirect, request
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse
from  .models import Post
 
 
def home(request):
    postList = Post.objects.filter(visible='1')
    paginator = Paginator(postList, 50)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
 
    context = {
        "posts": posts,
        "title": "Главная страница блога",
        "desc": "Описание для главной страницы",
        "key": "ключевые, слова",
    }
    return render(request, "partial/home.html", context)
 
def single(request, post_id):

    try: 
        a = Post.objects.get( id = post_id )
    except:
        raise Http404("Статья не найдена!")

    latest_comments_single = a.comment_set.order_by('-id')[:10]

    return render(request, 'partial/single.html', {'post': a, 'latest_comments_single': latest_comments_single })

def leave_comment(request, post_id):
    try: 
        a = Post.objects.get( id = post_id )
    except:
        raise Http404("Страница не найдена!")

    a.comment_set.create(author = request.POST['name'], comment_text = request.POST['text'])

    return HttpResponseRedirect(reverse('post:single', args = (a.id,)))