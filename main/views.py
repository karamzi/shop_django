from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import BallsSerializers, BagsSerializers, ShoesSerializers, AccessoriesSerializers

from .models import Balls, Bags, Shoes, Accessories, Orders, Cart


class BallsViews(APIView):

    def get(self, request):
        balls = Balls.objects.all()
        if 'subcategory' in request.GET:
            balls = balls.filter(subcategory=request.GET['subcategory'])
        serializers = BallsSerializers(balls, many=True)
        return Response(serializers.data)


class BallView(APIView):

    def get(self, request, vendor_code):
        try:
            ball = Balls.objects.get(vendor_code=vendor_code)
            serializer = BallsSerializers(ball)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class BagsView(APIView):

    def get(self, request):
        bags = Bags.objects.all()
        serializers = BagsSerializers(bags, many=True)
        return Response(serializers.data)


class BagView(APIView):

    def get(self, request, vendor_code):
        try:
            bag = Bags.objects.get(vendor_code=vendor_code)
            serializer = BagsSerializers(bag)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class ShoesView(APIView):

    def get(self, request):
        shoes = Shoes.objects.all()
        serializers = ShoesSerializers(shoes, many=True)
        return Response(serializers.data)


class CurrentShoesView(APIView):

    def get(self, request, vendor_code):
        try:
            shoes = Shoes.objects.get(vendor_code=vendor_code)
            serializer = ShoesSerializers(shoes)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return HttpResponse(status=404)


class AccessoriesView(APIView):

    def get(self, request):
        accessory = Accessories.objects.all()
        serializers = AccessoriesSerializers(accessory, many=True)
        return Response(serializers.data)


class AccessoryView(APIView):

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

        return HttpResponse(status=200)
