from django.shortcuts import render, redirect
from stores.models import Store, Time
import datetime
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def home(request):

	return render(request, 'customers/home.html')

def search(request):

	query=request.GET['search']
	object_list=Store.objects.filter(store_name__icontains=query) | Store.objects.filter(locality__icontains=query) | Store.objects.filter(city__icontains=query) | Store.objects.filter(pincode__icontains=query)
	context={
		'object_list': object_list
	}

	return render(request, 'customers/search.html', context)

def bookappointment(request, id):

	stores=Store.objects.filter(pk=id).first()
	times=Time.objects.filter(store=stores)
	sendtimes=[]	
	for t in times:
		if t.limit>0 and t.starttime>datetime.datetime.now().time():
			sendtimes.append(t)

	if request.method=="POST":
		time=request.POST.get('time', '')
		stores=Store.objects.get(pk=id)
		email=request.POST.get('email', '')
		name=request.POST.get('name', '')
		t=Time.objects.filter(store=stores).filter(starttime=time).first()
		t.limit=t.limit-1
		t.save()
		print(t.limit)

		send_mail(
				'Appointement booking for '+stores.store_name,
				'''Dear Customer,\n\nPlease show this mail at '''+stores.store_name+''' to confirm that you have an appointment at '''+time+'''\n\nRegards,\nTeam Stay Safe''',
				settings.EMAIL_HOST,
				[email],
			)
		messages.success(request, "Appointement booked successfully!")
		return redirect('account', id)

	context={
		'timeslots':sendtimes
	}
	return render(request, 'customers/bookappointment.html', context)