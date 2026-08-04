from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),


    path('categories/', views.category_list, name='category_list'),
    path('categories/add/', views.add_category, name='add_category'),

    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.add_product, name="add_product"),
    path("products/edit/<int:pk>/", views.edit_product, name="edit_product"),

    path("suppliers/", views.supplier_list, name="supplier_list"),
    path("suppliers/add/", views.add_supplier, name="add_supplier"),
    path("products/delete/<int:pk>/", views.delete_product, name="delete_product"),
]