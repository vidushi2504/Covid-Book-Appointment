from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Store, Time
from datetime import timedelta
import datetime

# Create your views here.
def user_login(request):

	if request.method=="POST":
		user_name=request.POST.get('username', '')
		user_password=request.POST.get('password', '')
		user=authenticate(username=user_name, password=user_password)
		if user:
			if user.last_login == None:
				login(request, user)
				messages.success(request, "Logged In")
				return redirect("editdetails")
			else:
				login(request, user)
				messages.success(request, "Logged In")
				details=Store.objects.filter(user=request.user).first()
				return redirect("account", details.id)
		else:
			messages.error(request, "Invalid Credentials")
			return redirect("login")

	return render(request, 'stores/login.html')

def user_logout(request):
	logout(request)
	return redirect("/")

def user_signup(request):

	if request.method=="POST":
		mail=request.POST.get('email', '')
		username=request.POST.get('username', '')
		password=request.POST.get('password', '')
		confirmpassword=request.POST.get('confirmpassword', '')
		userCheck=User.objects.filter(username=username) | User.objects.filter(email=mail)
		if userCheck:
			messages.error(request, "Username or Email already exists!")
			return redirect("signup")
		else:
			if password==confirmpassword:
				user_obj=User.objects.create_user(password=password, email=mail, username=username)
				user_obj.save()
				messages.success(request, "Signed Up successfully")
				return redirect("login")
			else:
				messages.error(request, "Passwords don't match!")
				return redirect("signup")
	return render(request, 'stores/signup.html')

def account(request, id):

	details=Store.objects.filter(pk=id).first()
	timeslots=[]
	if details:
		times=Time.objects.filter(store_id=details.id)
		if details.date!=datetime.datetime.now().date():
			details.date=datetime.datetime.now().date()
			times.delete()
			ot=details.openingtime
			ct=details.closingtime
			et=(datetime.datetime.combine(datetime.date(1,1,1),ot) + datetime.timedelta(hours=1)).time()
			while ot<ct:
				Time.objects.create(store=details, starttime=ot, endtime=et, limit=details.limit)
				ot=(datetime.datetime.combine(datetime.date(1,1,1),ot) + datetime.timedelta(hours=1)).time()
				et=(datetime.datetime.combine(datetime.date(1,1,1),et) + datetime.timedelta(hours=1)).time()
		timeslots=Time.objects.filter(store_id=details.id)	
	context={
		'details':details,
		'timeslots':timeslots
	}

	return render(request, 'stores/account.html', context)

def edit(request):

	details=Store.objects.filter(user=request.user).first()
	if request.method=="POST":
		if not details:
			storename=request.POST.get('storename', '')
			category=request.POST.get('category', '')
			address1=request.POST.get('address1', '')
			locality=request.POST.get('locality', '')
			city=request.POST.get('city', '')
			pincode=request.POST.get('pincode', '')
			contact=request.POST.get('contactnumber', '')
			description=request.POST.get('description', '')
			opening_time=request.POST.get('openingtime', '')
			closing_time=request.POST.get('closingtime', '')
			limit=int(request.POST.get('limit', ''))
			mail=request.POST.get('storemail', '')
			store_obj=Store.objects.create(user=request.user, store_name=storename, address1=address1, locality=locality, city = city, pincode = pincode, description=description, category=category, contact=contact, openingtime=opening_time, closingtime=closing_time, limit=limit, store_email=mail)
			store_obj.save()
			details=Store.objects.filter(user=request.user).first()
			return redirect("account", details.id)
		else:
			details.store_name=request.POST.get('storename', '')
			details.address1=request.POST.get('address1', '')
			details.locality=request.POST.get('locality', '')
			details.city=request.POST.get('city', '')
			details.pincode=request.POST.get('pincode', '')
			details.description=request.POST.get('description', '')
			details.category=request.POST.get('category', '')
			details.contact=request.POST.get('contactnumber', '')
			details.openingtime=request.POST.get('openingtime', '')
			details.closingtime=request.POST.get('closingtime', '')
			limit=request.POST.get('limit', '')
			details.store_email=request.POST.get('storemail', '')
			details.save()
			messages.success(request, "Changes made successfully!")
			return redirect("account", details.id)


	context={
		'details':details
	}

	return render(request, 'stores/editdetails.html', context)