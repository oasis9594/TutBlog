from django.shortcuts import render, redirect
from Blogs.models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Blogs.forms import BlogForm, CommentForm
from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required(login_url="/login/")
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
	x=1
	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs , 'x':x})

def popular(request):
	blog_list = Blog.objects.order_by('-votes')
	page = request.GET.get('page', 1)
	x=2
	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs , 'x':x})

def recent(request):
	blog_list = Blog.objects.order_by('-updated')
	page = request.GET.get('page', 1)
	x=3
	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs , 'x':x})

def data_structures(request):
	blog_list = Blog.objects.filter(category__in=[1])
	page = request.GET.get('page', 1)
	x=4
	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs , 'x':x})

def algorithms(request):
	blog_list = Blog.objects.filter(category__in=[2])
	page = request.GET.get('page', 1)
	x=5
	paginator = Paginator(blog_list, 5)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request, "blog_list.html", { 'blogs': blogs , 'x':x})
	
def blog_detail(request, blog_id):
	blog=Blog.objects.get(pk=blog_id)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if(form.is_valid()):
			instance = form.save(commit=False)
			instance.user = request.user
			instance.blog=blog
			instance.save()
			return redirect('blog_detail', blog_id)
	else:
		form=CommentForm()

	return render(request,"blog_detail.html", {
        'form': form,'blog': blog,
    })

@login_required(login_url="/login/")
def vote(request, blog_id):
	blog=Blog.objects.get(pk=blog_id)
	user = request.user
	vote_val = request.POST.get("vote", "")
	
	if vote_val == 'up':
		if blog.upvotes.filter(id=user.id).exists():
			blog.upvotes.remove(user)
		else:
			if blog.downvotes.filter(id=user.id).exists():
				blog.downvotes.remove(user)
			blog.upvotes.add(user)
	else:
		if blog.downvotes.filter(id=user.id).exists():
			blog.downvotes.remove(user)
		else:
			if blog.upvotes.filter(id=user.id).exists():
				blog.upvotes.remove(user)
			blog.downvotes.add(user)
	user.profile.contribution -= blog.total_votes
	blog.total_votes = blog.upvotes.count() - blog.downvotes.count()
	user.profile.contribution += blog.total_votes
	blog.save()
	return redirect('blog_detail', blog_id)


