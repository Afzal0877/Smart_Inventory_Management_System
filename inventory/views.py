from django.shortcuts import render, redirect
from .models import Category, Product, Supplier
from .forms import ProductForm, SupplierForm


def dashboard(request):
    return render(request, 'inventory/dashboard.html')



def category_list(request):
    categories = Category.objects.all()

    return render(request, 'inventory/category_list.html', {
        'categories': categories
    })


def add_category(request):

    if request.method == "POST":

        Category.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )

        return redirect('category_list')

    return render(request, 'inventory/category_form.html')
def product_list(request):
    products = Product.objects.all()

    return render(request, "inventory/product_list.html", {
        "products": products
    })
def add_product(request):

    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form = ProductForm()

    return render(request, "inventory/product_form.html", {
        "form": form
    })
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, "inventory/supplier_list.html", {
        "suppliers": suppliers
    })


def add_supplier(request):

    if request.method == "POST":
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("supplier_list")

    else:
        form = SupplierForm()

    return render(request, "inventory/supplier_form.html", {
        "form": form
    })