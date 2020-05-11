from django.shortcuts import render, redirect, get_object_or_404
from .models import Req
from django.utils import timezone

# Create your views here.
def main(request):
    return render(request, 'main.html')

def profile(request):
    return render(request, 'profile.html')

# ---------------------------------------------------

def req(request):
    reqs = Req.objects
    return render(request, 'req.html', {'reqs': reqs})

def detail(request, req_id):
    details = get_object_or_404(Req, pk=req_id)
    return render(request, 'detail.html', {'details': details})

def new(request):
    return render(request, 'new.html')

def create(request):
    req = Req()
    req.title = request.GET['title']
    req.body = request.GET['body']
    req.pub_date = timezone.datetime.now()
    req.save()
    return redirect('req')

# ---------------------------------------------

def edit(request, req_id):
    req = get_object_or_404(Req, pk=req_id)
    return render(request, 'edit.html', {'req': req})

def update(request, req_id):
    req = get_object_or_404(Req, pk=req_id)
    req.title = request.GET['title']
    req.body = request.GET['body']
    req.pub_date = timezone.datetime.now()
    req.save()
    return redirect('req')

def delete(request, req_id):
    req = get_object_or_404(Req, pk=req_id)
    req.delete()
    return redirect('req')