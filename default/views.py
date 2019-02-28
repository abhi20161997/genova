from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Tablet,Injection,Medicine, Member, Address
from .forms import Login, Sign_up
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages



def index(request):
    return render(request, 'default/index.html')

def contact(request):
    return render(request, 'default/contact.html')

def about(request):
    return render(request, 'default/about.html')

def tablets(request):
	tablets = Tablet.objects.all()
	return render(request, 'default/tablets.html',{"tablets": tablets})

def injections(request):
	injections = Injection.objects.all()
	return render(request, 'default/injections.html',{"injections": injections})

def medicines(request):
	medicines = Medicine.objects.all()
	return render(request, 'default/medicines.html',{"medicines": medicines})

def tab_product(request,product_id):
	product = Tablet.objects.get(id=product_id)
	context = {'product':product}
	if product.price_25:
		p25 = 25 * product.price_25
		context['p25'] = p25
	if product.price_50:
		p50 = 50 * product.price_50
		context['p50'] = p50
	if product.price_100:
		p100 = 100 * product.price_100
		context['p100'] = p100
	print product_id
	return render(request, 'default/product_tab.html',context)

def inj_product(request,product_id):
	product = Injection.objects.get(id=product_id)	
	context = {'product':product}
	if product.price_25:
		p25 = 25 * product.price_25
		context['p25'] = p25
	if product.price_50:
		p50 = 50 * product.price_50
		context['p50'] = p50
	if product.price_100:
		p100 = 100 * product.price_100
		context['p100'] = p100
	return render(request, 'default/product_inj.html', context)

def med_product(request,product_id):
	product = Medicine.objects.get(id=product_id)
	context = {'product':product}
	if product.price_25:
		p25 = 25 * product.price_25
		context['p25'] = p25
	if product.price_50:
		p50 = 50 * product.price_50
		context['p50'] = p50
	if product.price_100:
		p100 = 100 * product.price_100
		context['p100'] = p100
	return render(request, 'default/product_med.html', context)


def contact_response(request):
	if request.method == "POST":
		name = request.POST['NAME']
		email = request.POST['EMAIL']
		phone = request.POST['PHONE']
		subject = request.POST['SUBJECT']
		message = request.POST['MESSAGE']
		# print name, email,phone, subject, message

	return render(request, 'default/contact_form.html')

def sign_in(request):
	if request.user.is_anonymous:
		if request.method == "POST":
			form = Login(request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				current_user = authenticate(username=username, password=password)
				if current_user:
					login(request, current_user)
					current_user = request.user
					current_member = Member.objects.get(user = current_user)
					# messages.success(request, "Welcome")
					return redirect("/genova/")
				else:
					messages.error(request, "Please check your credentials")
			else:
				messages.error(request, "Please check the data you entered")
		else:
			form = Login()
			return render(request, 'default/login.html', {'form':form})
	else:
		return HttpResponse('You are already signed in')

def sign_up(request):
	if request.user.is_anonymous:
		if request.method == "POST":
			form = Sign_up(request.POST)
			if form.is_valid():
				name = form.cleaned_data.get('name')
				email = form.cleaned_data.get('email')
				username = form.cleaned_data.get('username')
				mobile_number = form.cleaned_data.get('mobile_number')
				password = form.cleaned_data.get('password')
				password2 = form.cleaned_data.get('repeat_password')
				if password == password2:
					new_user = User.objects.create_user(username=username, password=password)
					new_user.save()
					member = Member(name = name, user=new_user, email=email, mobile_number=mobile_number)
					member.save()
					return redirect("/genova/sign_in")
				else:
					return HttpResponse("The passwords do not match")
			else:
				return HttpResponse("Please check the data that you have entered")
		else:
			form=Sign_up()
			return render(request, 'default/sign_up.html', {'form':form})
	else:
		return redirect('/genova/')

def cart(request):
	if request.user.is_authenticated:
		current_user = request.user
		current_member = Member.objects.get(user = current_user)
		item_list = []
		tablet_list = current_member.tablet_bought.all()
		injection_list = current_member.injection_bought.all()
		medicine_list = current_member.medicine_bought.all()

		return render(request, 'default/cart.html', {
			'tablets':tablet_list,
			'injections':injection_list,
			'medicines':medicine_list,
			})
	else:
		return redirect('/genova/sign_in')

def sign_out(request):
	logout(request)
	messages.success(request, "You have been successfully logged out")
	return redirect('/genova/sign_in')



def add_tablet_to_cart(request, product_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = request.POST.get('products_id')
			current_user = request.user
			current_member = Member.objects.get(user=current_user)
			tablet = Tablet.objects.get(pk = product_id)
			current_member.tablet_bought.add(tablet)
			tablet.purchase_quantity=data
			tablet.save(update_fields=["purchase_quantity"])
			messages.success(request, "Tablet added to cart!")
			return cart(request)
		return redirect('/genova/tablets')
	else:
		return redirect('/genova/sign_in')

def remove_tablet_from_cart(request, product_id):
	current_user = request.user
	current_member = Member.objects.get(user=current_user)
	tablet = Tablet.objects.get(pk = product_id)
	current_member.tablet_bought.remove(tablet)
	messages.error(request, "Tablet removed from cart")
	return redirect('/genova/cart')


def add_injection_to_cart(request, product_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = request.POST.get('products_id')
			current_user = request.user
			current_member = Member.objects.get(user=current_user)
			injection = Injection.objects.get(pk = product_id)
			current_member.injection_bought.add(injection)
			injection.purchase_quantity=data
			injection.save(update_fields=["purchase_quantity"]) 
			messages.success(request, "Injection added to cart!")
		return redirect('/genova/injections')
	else:
		return redirect('/genova/sign_in')


def remove_injection_from_cart(request, product_id):
	current_user = request.user
	current_member = Member.objects.get(user=current_user)
	injection = Injection.objects.get(pk = product_id)
	current_member.injection_bought.remove(injection)
	messages.error(request, "Injection removed from cart")
	return redirect('/genova/cart')


def add_medicine_to_cart(request,product_id):
	if request.user.is_authenticated:
		if request.method == 'POST':
			data = request.POST.get('products_id')
			current_user = request.user
			current_member = Member.objects.get(user=current_user)
			medicine = Medicine.objects.get(pk = product_id)
			current_member.medicine_bought.add(medicine)
			medicine.purchase_quantity=data
			medicine.save(update_fields=["purchase_quantity"]) 
			messages.success(request, "Medicine added to cart!")
		return redirect('/genova/medicines')
	else:
		return redirect('/genova/sign_in')


def remove_medicine_from_cart(request, product_id):
	current_user = request.user
	current_member = Member.objects.get(user=current_user)
	medicine = Medicine.objects.get(pk = product_id)
	current_member.medicine_bought.remove(medicine)
	messages.error(request, "Medicine removed from cart")
	return redirect('/genova/cart')


def alpha(request,alpha):
	medicines = Medicine.objects.filter(brand=alpha)
	tablets = Tablet.objects.filter(brand=alpha)
	injections = Injection.objects.filter(brand=alpha)
	return render(request, 'default/brands.html',{"medicines": medicines,
		"tablets":tablets, "injections":injections})
   