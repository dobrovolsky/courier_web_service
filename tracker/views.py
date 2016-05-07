from django.core.paginator import Paginator
from django.shortcuts import render

from tracker.models import User, Tracker


def index(request):
    context = {}
    return render(request, 'tracker/index.html', context)


def users(request, page=1):
    page = int(page)
    users_by_id = User.objects.all()
    p = Paginator(users_by_id, 2)
    page1 = p.page(page)
    context = {
        'users': page1,
        'paginator': p,
        'page': page,
    }
    return render(request, 'tracker/users.html', context)


def user(request, user_id, page=1):
    user_id = int(user_id)
    page = int(page)
    user_by_id = Tracker.objects.all().filter(user_id=user_id)
    name = User.objects.get(pk=user_id).first_name
    p = Paginator(user_by_id, 2)
    page1 = p.page(page)
    context = {
        'name': name,
        'trackers': page1,
        'paginator': p,
        'page': page,
        'user_id': user_id,
    }
    return render(request, 'tracker/user.html', context)


def tracker(request, track_id):
    track = Tracker.objects.get(pk=int(track_id))
    context = {
        'ob': track,
    }
    return render(request, 'tracker/tracker.html', context)
