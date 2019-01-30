from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
	blogs= Blog.objects
	return render(request,"allblogs.html",{'blogs':blogs})

def blog_details(request,blog_id):
	blogdetails = get_object_or_404(Blog,pk=blog_id)
	return render(request,'blog_details.html',{'blog':blogdetails})