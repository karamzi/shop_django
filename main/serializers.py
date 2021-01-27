from rest_framework import serializers

from .models import Balls, Bags, Shoes, Img, Accessories, BallWeight, ShoesSize, PopularProduct


class ImgSerializers(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Img
        fields = ('img',)


class WeightSerializers(serializers.ModelSerializer):
    class Meta:
        model = BallWeight
        fields = ('weight',)


class BallsSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    img = serializers.SerializerMethodField()
    weight = WeightSerializers(many=True)

    def get_img(self, obj):
        return 'http://127.0.0.1:8000' + obj.img.url

    class Meta:
        model = Balls
        exclude = ('id',)


class BagsSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return 'http://127.0.0.1:8000' + obj.img.url

    class Meta:
        model = Bags
        exclude = ('id',)


class SizeSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShoesSize
        fields = ('size',)


class ShoesSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    img = serializers.SerializerMethodField()
    size = SizeSerializers(many=True)

    def get_img(self, obj):
        return 'http://127.0.0.1:8000' + obj.img.url

    class Meta:
        model = Shoes
        exclude = ('id',)


class AccessoriesSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    img = serializers.SerializerMethodField()

    def get_img(self, obj):
        return 'http://127.0.0.1:8000' + obj.img.url

    class Meta:
        model = Accessories
        exclude = ('id',)


class PopularProductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    def get_product(self, obj):
        if obj.ball:
            return BallsSerializers(obj.ball).data
        if obj.shoes:
            return ShoesSerializers(obj.shoes).data
        if obj.accessory:
            return AccessoriesSerializers(obj.accessory).data
        if obj.bag:
            return BagsSerializers(obj.bag).data
        return None

    class Meta:
        model = PopularProduct
        fields = ('product',)
