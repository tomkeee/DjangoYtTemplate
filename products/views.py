from django.shortcuts import render, Http404
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

from .forms import ProductModelForms
from .models import Product

def home_view(request,*args,**kwargs):
    return render (request,"home.html",{})

def product_detail_view(request, pk):
    # obj = Product.objects.get(id=id)
    try:
        obj = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404 # render html page, with HTTP status code of 404
    # try:
    #     obj = Product.objects.get(id=id)
    # except:
    #     raise Http404
    # return HttpResponse(f"Product id {obj.id}")
    # return render(request, "products/product_detail.html", {"object": obj})
    return render(request, "accounts/detail.html", {"object": obj})


# def product_create_view(request,*args,**kwargs):
#     my_form=ProductForms(request.POST or None)
#     if my_form.is_valid():
#         title_from_input=my_form.cleaned_data.get("Title")
#         Product.objects.create(title=title_from_input)

#     context={}
#     return render(request,"forms.html",context)



# def product_create_view(request,*args,**kwargs):
#     form = ProductForms(request.POST or None)
#     if form.is_valid():
#         data = form.cleaned_data
#         Product.objects.create(**data)
#     context={
#         "form":form
#     }
#     return render(request,"forms.html",context)

@login_required
def product_create_view(request,*args,**kwargs):
    x = ProductModelForms(request.POST or None)
    if x.is_valid():
        obj=x.save(commit=False)
        obj.save()
        x=ProductModelForms()
    context={"form":x}
    return render(request,"forms.html",context)