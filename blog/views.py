from django.shortcuts import render , get_object_or_404
from .models import Blog
from predict.models import database

def all_blogs(request):
    list_disease = []
    disease_obj = database.objects.all()
    for d in disease_obj:
        list_disease.append(d.disease)
    blogs=Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs':blogs,"disease": list_disease})

def detail(request, blog_id):
    list_disease = []
    disease_obj = database.objects.all()
    for d in disease_obj:
        list_disease.append(d.disease)
    blog =get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog': blog,"disease": list_disease})

