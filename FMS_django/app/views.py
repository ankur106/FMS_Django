from django.shortcuts import render,redirect

#email
from FMS_Django.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from app.forms import AdminRegisterForm

from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required


#models
from app.models import Customer,Product

from django.contrib import messages

def home(request):
	return render(request, 'app/index_fms.html')


@login_required(login_url='loginAdmin')
def sendEmail(request):
	if request.method == "POST":
		msg = request.POST['msg']
		recepient = list(map(lambda x: x.email,Customer.objects.all()))
		print(recepient)       
		if msg:
			send_mail("test", msg, EMAIL_HOST_USER, recepient)
			return redirect('success')
		else:
			return render(request, 'app/sendEmail.html',{'err':'Error'})


	return render(request, 'app/sendEmail.html')

	

def success(request):
	return render(request, 'app/success.html')



@login_required(login_url='loginAdmin')
def dashboard(request):
	return render(request, 'app/dashboard.html')





def createAdmin(request):

	if request.method == 'GET':
		return render(request, 'app/createAdmin.html',{'form':AdminRegisterForm()})

	else:
		form = AdminRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('dashboard')
		else:
			return render(request, 'app/createAdmin.html',{
         		 	'form' : AdminRegisterForm(),
         		 	'err' : 'Please Check the fields!!'
         		})




def logoutAdmin(request):

	if request.method == "POST":
		logout(request)
		return redirect('home')



def loginAdmin(request):

	if request.method == "GET":
		return render(request, 'app/login.html',{'form':AuthenticationForm()})

	else:
		uname = request.POST['username']
		pwd = request.POST['password']

		user = authenticate(request,username=uname,password=pwd)

		if user is None:
			return render(request, 'app/login.html',{'form':AuthenticationForm(),'err':'username and password is Mismatch!!'})
		else:
			login(request, user)
			return redirect('dashboard')



@login_required(login_url='loginAdmin')
def myfun(request):
	productObjList = Product.objects.all()
	productTypeList = set(list(map(lambda x: x.productType,productObjList)))
	productNameList = list(map(lambda x: x.productName,productObjList))

	# productIdList = Product.objects.filter(productType=request)



    
	if request.method == 'POST':

		
		# print(productTypeList)
		# print(productNameList)
		productName = request.POST['p_name']
		productType = request.POST['p_type']
		productList = Product.objects.filter(productName=productName,productType=productType)
		# print('first:-',productList.first())
		if productList.first():

			pId = productList.first().productId
			# print(pId)

			customerList = Customer.objects.filter(productId=pId)
			customerEmailList = list(map(lambda x: x.email,customerList))
			# print(customerList)
			print(customerEmailList)
			formLink = request.POST['formLink']
			msg = request.POST['msg']
			# print(msg)
			# print(formLink)
			msg = msg  + formLink

			if not msg and not formLink:
				messages.error(request, 'Please Fill all fields',extra_tags='alert')
				render(request, 'app/try.html',{
					   'productTypeList' : productTypeList,
					   'productNameList' : productNameList


					})
				
			else:
				send_mail("Survey", msg, EMAIL_HOST_USER, customerEmailList)
				return redirect('success')
				
		else:
			messages.error(request, 'No Customer For selected productType & productName!!',extra_tags='alert')
			print('errrr')
			render(request, 'app/try.html',{
					   'productTypeList' : productTypeList,
					   'productNameList' : productNameList


					})




		

	return render(request, 'app/try.html',{
		  
		  'productTypeList' : productTypeList,
		  'productNameList' : productNameList

		})



