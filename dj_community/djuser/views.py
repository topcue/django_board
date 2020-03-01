from django.shortcuts import render, redirect
from .models import Djuser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm
# Create your views here.

def home(request):
	return render(request, "home.html")

def register(request):
	if request.method == "GET":
		return render(request, "register.html")
	elif request.method == 'POST':
		username = request.POST.get('username', None)
		useremail = request.POST.get('useremail', None)
		password = request.POST.get('password', None)
		re_password = request.POST.get('re-password', None)
		
		res_data = {}
		if not (username and useremail and password and re_password):
			res_data['error'] = '모든 값을 입력해야합니다.'
		elif password != re_password:
			res_data['error'] = '비밀번호가 다릅니다.'
		# 아이디 중복 체크 구현
		else:
			djuser = Djuser(
                username = username,
                useremail = useremail,
                password = make_password(password)
            )
			djuser.save()
			return redirect("/home")

		return render(request, 'register.html', res_data)

def login(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			request.session['user'] = form.user_id
			return redirect('/home/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})
		
def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    
    return redirect('/home/')

# EOF
