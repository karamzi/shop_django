from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, DetailView
from django.core.mail import send_mail
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BallsSerializers, BagsSerializers, ShoesSerializers, AccessoriesSerializers, \
    PopularProductSerializer

from .models import Balls, Bags, Shoes, Accessories, Orders, Cart, PopularProduct


class BallsAPIViews(APIView):

    def get(self, request):
        balls = Balls.objects.all()
        serializers = BallsSerializers(balls, many=True)
        return Response(serializers.data)


class BallAPIView(APIView):

    def get(self, request, vendor_code):
        try:
            ball = Balls.objects.get(vendor_code=vendor_code)
            serializer = BallsSerializers(ball)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class BagsAPIView(APIView):

    def get(self, request):
        bags = Bags.objects.all()
        serializers = BagsSerializers(bags, many=True)
        return Response(serializers.data)


class BagAPIView(APIView):

    def get(self, request, vendor_code):
        try:
            bag = Bags.objects.get(vendor_code=vendor_code)
            serializer = BagsSerializers(bag)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class ShoesAPIView(APIView):

    def get(self, request):
        shoes = Shoes.objects.all()
        serializers = ShoesSerializers(shoes, many=True)
        return Response(serializers.data)


class CurrentShoesAPIView(APIView):

    def get(self, request, vendor_code):
        try:
            shoes = Shoes.objects.get(vendor_code=vendor_code)
            serializer = ShoesSerializers(shoes)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class AccessoriesAPIView(APIView):

    def get(self, request):
        accessory = Accessories.objects.all()
        serializers = AccessoriesSerializers(accessory, many=True)
        return Response(serializers.data)


class AccessoryAPIView(APIView):

    def get(self, request, vendor_code):
        try:
            accessory = Accessories.objects.get(vendor_code=vendor_code)
            serializer = AccessoriesSerializers(accessory)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        cart = json.loads(request.POST['cart'])
        order = Orders.objects.create(name=request.POST['name'], phone=request.POST['phone'],
                                      email=request.POST['email'], total_price=request.POST['totalPrice'])
        for item in cart:
            product = Cart()
            product.vendor_code = item['vendor_code']
            product.name = item['name']
            product.size = item['size']
            product.quantity = item['quantity']
            product.price = item['price']
            product.order = order
            product.save()
        send_mail('Новый заказ', 'На сайте появился новый заказ', 'federation.bratsk@gmail.com', ['aleka-spb@mail.ru'],
                  fail_silently=False)
        return HttpResponse(status=200)


class PopularProductAPIView(APIView):

    def get(self, request):
        popular_products = PopularProduct.objects.all()[:4]
        serializer = PopularProductSerializer(popular_products, many=True)
        return Response(serializer.data)


def index(request):
    popular_products = PopularProduct.objects.all()[:4]
    serializer = PopularProductSerializer(popular_products, many=True)
    context = {
        'popular_products': serializer.data
    }
    return render(request, 'index.html', context)


class BallsView(ListView):
    template_name = 'balls.html'
    model = Balls


class BallView(DetailView):
    template_name = 'ball.html'
    model = Balls
    slug_field = 'vendor_code'


class BagsView(ListView):
    template_name = 'bags.html'
    model = Bags


class BagView(DetailView):
    template_name = 'bag.html'
    model = Bags
    slug_field = 'vendor_code'


class ShoesView(ListView):
    template_name = 'shoes.html'
    model = Shoes


class CurrentShoesView(DetailView):
    template_name = 'current_shoes.html'
    model = Shoes
    slug_field = 'vendor_code'


class AccessoriesView(ListView):
    template_name = 'accessories.html'
    model = Accessories


class AccessoryView(DetailView):
    template_name = 'accessory.html'
    model = Accessories
    slug_field = 'vendor_code'


class BowlingSchoolView(TemplateView):
    template_name = 'bowling_school.html'
