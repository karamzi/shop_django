from django.urls import path
from django.conf.urls import url
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/1.0/balls/', views.BallsAPIViews.as_view()),
    path('api/1.0/ball/<int:vendor_code>/', views.BallAPIView.as_view()),
    path('api/1.0/bags/', views.BagsAPIView.as_view()),
    path('api/1.0/bag/<int:vendor_code>/', views.BagAPIView.as_view()),
    path('api/1.0/shoes/', views.ShoesAPIView.as_view()),
    path('api/1.0/shoes/<int:vendor_code>/', views.CurrentShoesAPIView.as_view()),
    path('api/1.0/accessories/', views.AccessoriesAPIView.as_view()),
    path('api/1.0/accessory/<int:vendor_code>/', views.AccessoryAPIView.as_view()),
    path('api/1.0/createOrder/', views.create_order),
    path('api/1.0/popularProduct/', views.PopularProductAPIView.as_view()),
    path('category/balls', views.BallsView.as_view()),
    path('ball/<slug:slug>', views.BallView.as_view()),
    path('category/bags', views.BagsView.as_view()),
    path('bag/<slug:slug>', views.BagView.as_view()),
    path('category/shoes', views.ShoesView.as_view()),
    path('shoes/<slug:slug>', views.CurrentShoesView.as_view()),
    path('category/accessories', views.AccessoriesView.as_view()),
    path('accessory/<slug:slug>', views.AccessoryView.as_view()),
    path('training', views.BowlingSchoolView.as_view()),
    path('sitemap', TemplateView.as_view(template_name='sitemap.txt')),
    path('robot', TemplateView.as_view(template_name='robot.txt')),
    url(r'^', views.index),
]
