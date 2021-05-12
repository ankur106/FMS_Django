from django.contrib import admin

# Register your models here.
from app.models import FBFormType,FBForm,Customer,Product,Branch,branchProduct


admin.site.register(FBFormType)
admin.site.register(FBForm)
admin.site.register(Branch)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(branchProduct)