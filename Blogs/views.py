from django.shortcuts import render, redirect
from Blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Blogs.forms import BlogForm
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url="login/")
def create_blog(request):
	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES)
		if(form.is_valid()):
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('myblogs')
	else:
		form=BlogForm

	return render(request,"create_blog.html", {
        'form': form,
    })

def blog_index(request):
	blog_list = Blog.objects.all()
	page = request.GET.get('page', 1)

	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs })

def popular(request):
	blog_list = Blog.objects.order_by('-votes')
	page = request.GET.get('page', 1)

	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs })

def recent(request):
	blog_list = Blog.objects.order_by('-updated')
	page = request.GET.get('page', 1)

	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs })

def data_structures(request):
	blog_list = Blog.objects.filter(category__in=[1])
	page = request.GET.get('page', 1)

	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs })

def algorithms(request):
	blog_list = Blog.objects.filter(category__in=[2])
	page = request.GET.get('page', 1)

	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs })
	
class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'blog_detail.html'