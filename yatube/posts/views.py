# posts/views.py
from django.shortcuts import render, get_object_or_404
# Импортируем модель, чтобы обратиться к ней
from .models import Post, Group
# кольво постов
PUB_VALUE = 10


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    posts = Post.objects.select_related()[:PUB_VALUE]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.group_list.all()[:PUB_VALUE]

    context = {
        'text': slug,
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
