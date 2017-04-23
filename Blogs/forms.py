from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from Blogs.models import Blog, Category, Tags, Comment
from django import forms
from django.forms import ModelForm
class BlogForm(forms.ModelForm):
	title = forms.CharField(label="Title", max_length=100,
		widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'title'}))
	body=forms.CharField(widget=SummernoteWidget(attrs={'class': 'form-control', 'name': 'body'}))
	category = forms.ModelMultipleChoiceField(label="Category", required=True, widget=forms.CheckboxSelectMultiple(
		attrs={'class': 'form-control', 'name': 'category'}), queryset=Category.objects.all())
	tags= forms.ModelMultipleChoiceField(label="Tags", widget=forms.CheckboxSelectMultiple(
		attrs={'class': 'form-control', 'name': 'tags'}), queryset=Tags.objects.all())
	class Meta:
		model = Blog
		fields = ('title', 'category', 'tags', 'body')

class CommentForm(forms.ModelForm):
	text = forms.CharField(label="Have something to say about this article?",
		widget=forms.Textarea(attrs={'class': 'md-textarea', 'name': 'comment', 'id': 'comment'}))
	class Meta:
		model = Comment
		fields = ('text',)		