from django.db import models

# Create your models here.

class FBFormType(models.Model):

	fbFormTypeId = models.CharField(primary_key=True,max_length=30,unique=True)
	fbFormTypeName = models.CharField(max_length=40)


	def __str__(self):
		return str(self.fbFormTypeName)




class FBForm(models.Model):

	FBFormId = models.CharField(primary_key=True,max_length=30,unique=True)
	FBFormLink = models.CharField(max_length=250)
	FBFormTypeId = models.ForeignKey(to=FBFormType, on_delete=models.CASCADE)



# class Customer(models.Model):
# 	branc





class Product(models.Model):
	productId = models.CharField(max_length=40,primary_key=True,unique=True)
	productName = models.CharField(max_length=40,blank=False)
	productType = models.CharField(max_length=40,blank=False)


class Branch(models.Model):

	branchId = models.CharField(primary_key=True,max_length=40,unique=True,blank=False)
	branchName = models.CharField(max_length=50,blank=False,unique=True)
	Address = models.CharField(max_length=100,blank=False)
	productId = models.ForeignKey(to=Product, on_delete=models.CASCADE)



class Customer(models.Model):

	branchId = models.ForeignKey(to=Branch, on_delete=models.CASCADE)
	userId = models.CharField(primary_key=True,blank=False,max_length=40)
	email = models.EmailField()
	PhoneNo = models.CharField(max_length=10)
	productId = models.ForeignKey(to=Product, on_delete=models.CASCADE)












