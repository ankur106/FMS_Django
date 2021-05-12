from django.shortcuts import render,redirect

#email
from FMS_Django.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from app.forms import AdminRegisterForm

from django.db import IntegrityError
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required






import pandas as pd

#models
from app.models import Customer,Product,FBForm

from django.contrib import messages

def home(request):
	return render(request, 'app/index_fms.html')


def survey_status(request):
	return render(request, 'app/survey_status.html')



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


@login_required(login_url='loginAdmin')
def dashboard(request):
	return render(request, 'app/dashboard.html')




@login_required(login_url='loginAdmin')
def generate_report(request):
	if request.method == 'GET':
		return render(request, 'app/generate_report.html')
	else:

		csvFile = request.FILES['csv_file']

		if not csvFile.name.endswith('.csv'):
			return render(request, 'app/generate_report.html',
						  {'err': 'Please upload the .csv file'})
		else:
			import pandas as pd
			global readCSV
			readCSV = pd.read_csv(csvFile)
			read = readCSV.copy()
			#print(readCSV.columns)
			# print(readCSV.values.tolist())
			# print({'test':readCSV})

			return render(request, 'app/generate_report.html', {'test': readCSV.columns})





def logoutAdmin(request):

	if request.method == "POST":
		logout(request)
		return redirect('home')





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


def loginAdmin(request):

	if request.method == "GET":
		return render(request, 'app/login.html',{'form':AuthenticationForm()})
	else:
		uname = request.POST['username']
		pwd = request.POST['password']

		user = authenticate(request,username=uname,password=pwd)

		if user is None:
			return render(request, 'app/login.html',{'form':AuthenticationForm(),'err':'* Please enter valid username and password'})
		else:
			login(request, user)
			return redirect('home')



@login_required(login_url='loginAdmin')
def generate_survey(request):
	productObjList = Product.objects.all()
	productTypeList = set(list(map(lambda x: x.productType,productObjList)))
	productNameList = list(map(lambda x: x.productName,productObjList))

	formObjList = FBForm.objects.all()
	formIdList = list(map(lambda x: x.FBFormId,formObjList))

	# productIdList = Product.objects.filter(productType=request)

	if request.method == 'POST':
		# print(productTypeList)
		# print(productNameList)
		productName = request.POST['p_name']
		productType = request.POST['p_type']
		formid = request.POST['f_id']

		productList = Product.objects.filter(productName=productName,productType=productType)
		# print('first:-',productList.first())
		if productList.first():

			form = FBForm.objects.get(FBFormId=formid)
			formLink = form.FBFormLink
			pId = productList.first().productId
			# print(pId)

			customerList = Customer.objects.filter(productId=pId)
			customerEmailList = list(map(lambda x: x.email,customerList))
			# print(customerList)
			print(customerEmailList)


			msg = request.POST['msg']
			# print(msg)
			# print(formLink)
			msg = msg  + " "+ formLink

			if not msg and not formLink:
				messages.error(request, 'Please Fill all fields',extra_tags='alert')
				render(request, 'app/try.html',{
					'productTypeList' : productTypeList,
					'productNameList' : productNameList,
					'formIdList': formIdList

				})

			else:
				send_mail("How much do you like our product/service? Share your experience!!!", msg,'fms-no-reply<fms.feedbackmanagementsystem@gmail.com>', customerEmailList)
				return redirect('survey_status')

		else:
			messages.error(request, 'No Customer For selected productType & productName!!',extra_tags='alert')
			print('errrr')
			render(request, 'app/try.html',{
				'productTypeList' : productTypeList,
				'productNameList' : productNameList,
				'formIdList': formIdList

			})

	return render(request, 'app/generate_survey.html',{

		'productTypeList' : productTypeList,
		'productNameList' : productNameList,
		'formIdList' : formIdList

	})


def uploadCSV(request):
	pass

from . import plots
def test(request):



	cols = readCSV.columns[:]

	print(request.POST)

	# print(request.POST['outlook'])

	myplotdata = []

	myplots = plots.plot(readCSV)

	print(cols)
	for col in cols:
		print(col+" gets  "+ request.POST[col])

		if(request.POST[col]=='none'):
			continue

		if(request.POST[col]=='bar'):
			s_c = col+'s_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]
			graph= myplots.bar(col,s_c_name,t_c_name)




		if (request.POST[col] == 'pie'):
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]
			graph = myplots.pie(col, s_c_name, t_c_name)

		if (request.POST[col] == 'l_regression'):
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]
			graph = myplots.l_regression(col, s_c_name, t_c_name)

		if (request.POST[col] == 'l_regression_twoc'):
			print("hiiiiiiiiiiii")
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]
			graph = myplots.l_regression_2c(col, s_c_name, t_c_name)

		if request.POST[col] == 'Bubble':
			print('Bubble in views')
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]

			print(s_c_name)
			print(t_c_name)

			graph = myplots.bubble_chart(col, s_c_name, t_c_name)

		if request.POST[col] == 'LineGraph':
			print('LineGraph in views')
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]

			print(s_c_name)
			print(t_c_name)

			graph = myplots.LineChart(col, s_c_name, t_c_name)

		if request.POST[col] == 'DotPlot':
			print('DotGraph in views')
			s_c = col + 's_c'
			s_c_name = request.POST[s_c]
			t_c = col + 't_c'
			t_c_name = request.POST[t_c]

			print(s_c_name)
			print(t_c_name)

			graph = myplots.DotPlot(col, s_c_name, t_c_name)

		myplotdata.append(graph)


	# print(len(myplotdata))
	return render(request, 'app/report.html', {'plotz': myplotdata })