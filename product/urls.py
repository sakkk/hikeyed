from django.urls import path

from product import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('add/', views.ProductAdd.as_view(), name='prodcut_add'),
    path('edit/<int:pk>/', views.ProductEdit.as_view(), name='product_edit'),
    path('del/<int:pk>', views.ProductDel.as_view(), name='product_del'),
]