from django.db import models

from User.models import Profile
from django.template.defaultfilters import slugify

from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True, unique=True)
	def __str__(self):
		return self.title
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

class Tags(models.Model):
	name = models.CharField(max_length=100, unique=True)
	def __str__(self):
		return self.name
class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	created = models.DateTimeField(db_index=True, auto_now_add=True)
	category = models.ManyToManyField(Category)
	updated = models.DateTimeField(db_index=True, auto_now=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tags, blank = True)
	upvotes = models.ManyToManyField(User, related_name='blog_upvotes')
	downvotes = models.ManyToManyField(User, related_name='blog_downvotes')
	total_votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.title

	@models.permalink
	def get_absolute_url(self):
		return ("blog-detail", [self.slug,])

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Blog, self).save(*args, **kwargs)

class Comment(models.Model):
	text = models.TextField()
	blog = models.ForeignKey(Blog)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text

class Reply(models.Model):
	text = models.TextField()
	comment = models.ForeignKey(Comment)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.text
		
	