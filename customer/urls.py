from django.urls import path

from customer import views

urlpatterns = [
    path('', views.CustomerList.as_view(), name='customer_list'),
    path('add/', views.CustomerAdd.as_view(), name='customer_add'),
    path('edit/<int:pk>/', views.CustomerEdit.as_view(), name='customer_edit'),
    path('del/<int:pk>/', views.CustomerDel.as_view(), name='customer_del'),
]