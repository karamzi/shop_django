from django.urls import path
from .views import BallsViews, BallView, BagsView, BagView, ShoesView, CurrentShoesView, AccessoriesView, AccessoryView, \
    create_order

urlpatterns = [
    path('api/1.0/balls/', BallsViews.as_view()),
    path('api/1.0/ball/<int:vendor_code>/', BallView.as_view()),
    path('api/1.0/bags/', BagsView.as_view()),
    path('api/1.0/bag/<int:vendor_code>/', BagView.as_view()),
    path('api/1.0/shoes/', ShoesView.as_view()),
    path('api/1.0/shoes/<int:vendor_code>/', CurrentShoesView.as_view()),
    path('api/1.0/accessories/', AccessoriesView.as_view()),
    path('api/1.0/accessory/<int:vendor_code>/', AccessoryView.as_view()),
    path('api/1.0/createOrder/', create_order)
]
