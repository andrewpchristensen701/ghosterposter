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