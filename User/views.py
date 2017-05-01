from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from User.forms import SignUpForm, UserForm, ProfileForm
from django.contrib.auth import login
from django.core.mail import send_mail
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User
from User.tokens import account_activation_token
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="/login/")
def dashboard(request):
	return render(request,"dashboard.html")
@login_required(login_url="/login/")
def myblogs(request):
	user=request.user
	blogs=user.blog_set.filter(isTut=False)
	tutorials=user.blog_set.filter(isTut=True)
	return render(request,"myblogs.html", { 'blogs': blogs, 'tutorials': tutorials, })
@login_required(login_url="/login/")
def profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		if user_form.is_valid():
			user_form.save()
			if profile_form.is_valid():
				profile_form.save()
				return redirect('user')
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"user.html", {
        'user_form': user_form,
        'profile_form': profile_form
    })
def profile_with_username(request, username):
	user=User.objects.get(username=username)
	return render(request,"profile.html", {
        'user': user,
    })
@login_required(login_url="/login/")
def notifications(request):
	return render(request,"notifications.html")
def home(request):
	return render(request,"index.html")
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your MySite Account'
			message = render_to_string('account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
			})
			#user.email_user(subject, message)
			send_mail(subject, message, 'oasis9594@gmail.com', [user.email], fail_silently=False)
			return redirect('account_activation_sent')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})

def account_activation_sent(request):
	return render(request, 'account_activation_sent.html')
def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.profile.email_confirmed = True
		user.save()
		login(request, user)
		return redirect('home')
	else:
		return render(request, 'account_activation_invalid.html')