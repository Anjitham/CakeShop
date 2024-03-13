from django.shortcuts import render,redirect
from django.views.generic import View
from shop.models import Cake,CakeVarient,Category
from shop.forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout

# lh:8000/signup/
# method:get,post
# form_class:registration form
class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"signup.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request,"signup.html",{"form":form})
        
# lh:8000/signin/
# method:get,post
# form_class:Login form
class SignInView(View):

    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render (request,"signin.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user_object=authenticate(request,username=u_name,password=pwd)
            if user_object:
                login(request,user_object)
                return redirect("index")
        return render(request,"signin.html",{"form":form})
    
# lh:8000/
# method:get
class IndexView(View):

    def get(self,request,*args,**kwargs):
        qs=Category.objects.all()
        return render(request,"index.html",{"data":qs})

# lh:8000/category-list
# method:get
    
class CategoryListView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CakeVarient.objects.filter(cakecategory=id)
        return render (request,"category_item_list.html",{"data":qs})
    
# cakedetails
# lh:8000/cake/deatils
# method:get

class CakeDetailsView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=CakeVarient.objects.get(id=id)
        return render (request,"cake_detail.html",{"data":qs})

#lh:8000/ 
# class AddToBasketView(View):

   









