from django.urls import path
from . import views

urlpatterns = [
    path('api/1.0/balls/', views.BallsViews.as_view()),
    path('api/1.0/ball/<int:vendor_code>/', views.BallView.as_view()),
    path('api/1.0/bags/', views.BagsView.as_view()),
    path('api/1.0/bag/<int:vendor_code>/', views.BagView.as_view()),
    path('api/1.0/shoes/', views.ShoesView.as_view()),
    path('api/1.0/shoes/<int:vendor_code>/', views.CurrentShoesView.as_view()),
    path('api/1.0/accessories/', views.AccessoriesView.as_view()),
    path('api/1.0/accessory/<int:vendor_code>/', views.AccessoryView.as_view()),
    path('api/1.0/createOrder/', views.create_order),
    path('api/1.0/popularProduct/', views.PopularProductView.as_view()),
    path('', views.index),
]
