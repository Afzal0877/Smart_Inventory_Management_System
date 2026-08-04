from django.db.models import F
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, Supplier
from .forms import ProductForm, SupplierForm


def dashboard(request):

    total_products = Product.objects.count()
    total_categories = Category.objects.count()
    total_suppliers = Supplier.objects.count()

    low_stock_products = Product.objects.filter(
        quantity__lt=F("minimum_stock")
    )

    low_stock = low_stock_products.count()

    return render(request, "inventory/dashboard.html", {
        "total_products": total_products,
        "total_categories": total_categories,
        "total_suppliers": total_suppliers,
        "low_stock": low_stock,
        "low_stock_products": low_stock_products,
    })
    




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

    search = request.GET.get("search")

    if search:
        products = products.filter(name__icontains=search)

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
def edit_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("product_list")

    else:
        form = ProductForm(instance=product)

    return render(request, "inventory/product_form.html", {
        "form": form
    })
def delete_product(request, pk):

    product = get_object_or_404(Product, pk=pk)

    product.delete()

    return redirect("product_list")