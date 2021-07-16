from django.shortcuts import render
from .forms import User_creationform
from django.http import JsonResponse 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from .models import Post,User_creation


# Create your views here.

def registeruser(request):
	if request.method == 'POST':
		try:
			if request.POST["username"] and request.POST["password"]:
				if User.objects.filter(username=request.POST["username"]):
					return JsonResponse({"success":False,"error":"username already exist in our System"})
			username = User.objects.create_user(username=request.POST["username"],password=request.POST["password"])
			data = request.POST.copy()
			data.update({'username': username})
			form = User_creationform(data)
			if form.is_valid():
				form.save()
				user = authenticate(username=request.POST["username"],password=request.POST["password"])
				login(request,user)
				return JsonResponse({"success":True,"msg":"User Created Succesfully","username":str(username)})
			else:
				return JsonResponse({"success":False,"error":form.errors})
		except Exception as e:
			return JsonResponse({"success":False,"error":str(e)})
	return render(request,'index.html')

@login_required
def posts(request,data):
	try:
		if request.method == 'POST':
			user =  User.objects.filter(username=data)
			if user and request.POST['text']:
				user = User_creation.objects.get(username=user[0])
				a =  Post.objects.create(user=user,text=request.POST['text'])
				return JsonResponse({"success":True,"msg":"Succesfully"})
	except Exception as e:
		return JsonResponse({"success":False,"error":str(e)})

	return render(request,"post.html")