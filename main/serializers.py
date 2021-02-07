from rest_framework import serializers

from .models import Balls, Bags, Shoes, Img, Accessories, BallWeight, ShoesSize, PopularProduct


class ImgSerializers(serializers.ModelSerializer):
    img = serializers.SerializerMethodField()

    class Meta:
        model = Img
        fields = ('img',)


class BallsSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    weight = serializers.StringRelatedField(many=True)

    class Meta:
        model = Balls
        exclude = ('id',)


class BagsSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)

    class Meta:
        model = Bags
        exclude = ('id',)


class ShoesSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)
    size = serializers.StringRelatedField(many=True)

    class Meta:
        model = Shoes
        exclude = ('id',)


class AccessoriesSerializers(serializers.ModelSerializer):
    addition_img = ImgSerializers(many=True)

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
