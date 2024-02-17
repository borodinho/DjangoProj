from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.views.generic.edit import FormMixin

from .forms import CommentForm
from .models import ProjectItem, Comments
from django.views.generic.base import View

from portfsite.models import ProjectItem


# Create your views here.

def index(requset):
    projects = ProjectItem.objects.all()
    print(type(projects))
    context = {'projects': projects}
    return render(
        requset,
        'index.html',
        context=context
    )



def project_detail(request, id):
    obj = ProjectItem.objects.get(id=id)
    comments = Comments.objects.filter(new=obj, moderation=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.new = obj
            comment.save()
            return redirect('project', id=obj.id)
    else:
        form = CommentForm()

    return render(request, 'project.html', {'obj': obj, 'comments': comments, 'form': form})
