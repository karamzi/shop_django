from rest_framework import serializers

from .models import Balls, Bags, Shoes, Img, Accessories, BallWeight, ShoesSize


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
