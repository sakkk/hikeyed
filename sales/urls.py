from django.urls import path

from sales import views

urlpatterns = [
    path('detail_list/', views.SalesDetailList.as_view(), name='detail_list'),
    path('detail_add/', views.SalesDetailAdd.as_view(), name='detail_add'),
    path('detail_edit/<int:pk>/', views.SalesDetailEdit.as_view(), name='detail_edit'),
    path('detail_del/<int:pk>/', views.SalesDetailDel.as_view(), name='detail_del'),
]