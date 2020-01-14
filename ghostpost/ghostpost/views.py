from django.utils import timezone
from .models import GhostPost
from .forms import GhostAdd
from django.shortcuts import render, HttpResponseRedirect, reverse

def index(request):
    html = 'index.html'

    ghostposts = GhostPost.objects.all()

    return render(request, html, {'data': ghostposts})

def GhostPost_view(request):
    html = "ghost_add.html"
    if request.method == 'POST':
        form = GhostAdd(request.POST)
        if form.is_valid():

            data = form.cleaned_data

            GhostPost.objects.create(
                ghostTitle='help',
                body='help',
                is_boast=True,
                post_date=timezone.now()
                )

        return render(request,'end.html')
    else:
        form = GhostAdd()
        return render(request, html, {'form': form})

def upvotes(request, id):
    try:
        post = GhostPost.objects.get(id=id)
    except GhostPost.DoesNotExist():
        return HttpResponseRedirect('/')
    post.upvotes += 1
    post.total_votes += 1
    post.save()
    return HttpResponseRedirect('/')


def downvotes(request, id):
    try:
        post = GhostPost.objects.get(id=id)
    except GhostPost.DoesNotExist():
        return HttpResponseRedirect('/')
    post.downvotes += 1
    post.total_votes -= 1
    post.save()
    return HttpResponseRedirect('/')


def sort_is_a_boast(request):
    html = 'index.html'
    posts = GhostPost.objects.all().filter(
        is_boast=True).order_by('-post_date')
    return render(request, html, {'data': posts})


def sort_is_a_roast(request):
    html = 'index.html'
    posts = GhostPost.objects.all().filter(
        is_boast=False).order_by('-post_date')
    return render(request, html, {'data': posts})


def sort_all_posts(request):
    posts = GhostPost.objects.order_by('-total_votes')
    return render(request, 'index.html', {'data': posts})
