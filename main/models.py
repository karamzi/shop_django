from django.db import models
from datetime import datetime
from os.path import splitext


def get_img_path(instance, filename):
    if instance.__name__() == 'Balls' or hasattr(instance, 'ball'):
        return 'img/balls/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
    if instance.__name__() == 'Bags' or hasattr(instance, 'bag'):
        return 'img/bags/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
    if instance.__name__() == 'Shoes' or hasattr(instance, 'shoes'):
        return 'img/shoes/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])
    if instance.__name__() == 'Accessories' or hasattr(instance, 'accessories'):
        return 'img/accessories/%s%s' % (datetime.now().timestamp(), splitext(filename)[1])


class Img(models.Model):
    ball = models.ForeignKey('Balls', related_name='addition_img', verbose_name='Шар', blank=True, null=True,
                             on_delete=models.CASCADE)
    bag = models.ForeignKey('Bags', related_name='addition_img', verbose_name='Сумка', blank=True, null=True,
                            on_delete=models.CASCADE)
    shoes = models.ForeignKey('Shoes', related_name='addition_img', verbose_name='Обувь', blank=True, null=True,
                              on_delete=models.CASCADE)
    accessories = models.ForeignKey('Accessories', related_name='addition_img', verbose_name='Аксессуары', blank=True,
                                    null=True, on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Изображение', upload_to=get_img_path)

    def __str__(self):
        if self.ball:
            return self.ball.name
        if self.bag:
            return self.bag.name
        if self.shoes:
            return self.shoes.name

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class BallWeight(models.Model):
    weight = models.SmallIntegerField(verbose_name='Вес шара')

    def __str__(self):
        return str(self.weight)


class Balls(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикуль', default=0)
    category = models.CharField(verbose_name='Категория', default='ball', editable=False, max_length=5)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.SmallIntegerField(verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие', default=False)
    weight = models.ManyToManyField(BallWeight)
    img = models.ImageField(verbose_name='Изображение', upload_to=get_img_path)
    subcategory = (
        ('Storm', 'Storm'),
        ('Hammer', 'Hammer'),
        ('Motive', 'Motive'),
        ('Track', 'Track'),
    )
    subcategory = models.CharField(max_length=20, choices=subcategory)

    @staticmethod
    def __name__():
        return 'Balls'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = datetime.now().timestamp()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Шар'
        verbose_name_plural = 'Шары'


class Bags(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикуль', default=0)
    category = models.CharField(verbose_name='Категория', default='bag', editable=False, max_length=5)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.SmallIntegerField(verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие', default=False)
    img = models.ImageField(verbose_name='Изображение', upload_to=get_img_path)

    @staticmethod
    def __name__():
        return 'Bags'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = datetime.now().timestamp()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Сумка'
        verbose_name_plural = 'Сумки'


class ShoesSize(models.Model):
    size = models.DecimalField(verbose_name='Размер обуви', decimal_places=1, max_digits=3)

    def __str__(self):
        return str(self.size)


class Shoes(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикуль', default=0)
    category = models.CharField(verbose_name='Категория', default='shoes', editable=False, max_length=5)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.SmallIntegerField(verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие', default=False)
    size = models.ManyToManyField(ShoesSize, verbose_name='Размер обуви')
    img = models.ImageField(verbose_name='Изображение', upload_to=get_img_path)

    @staticmethod
    def __name__():
        return 'Shoes'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = datetime.now().timestamp()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Обувь'
        verbose_name_plural = 'Обувь'


class Accessories(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикуль', default=0)
    category = models.CharField(verbose_name='Категория', default='accessory', editable=False, max_length=5)
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание товара')
    price = models.SmallIntegerField(verbose_name='Цена')
    availability = models.BooleanField(verbose_name='Наличие', default=False)
    img = models.ImageField(verbose_name='Изображение', upload_to=get_img_path)

    @staticmethod
    def __name__():
        return 'Accessories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = datetime.now().timestamp()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Cart(models.Model):
    vendor_code = models.IntegerField(verbose_name='Артикуль', default=0)
    name = models.CharField(max_length=50, verbose_name='Название')
    size = models.CharField(max_length=10, verbose_name='Размер', blank=True, null=True)
    quantity = models.SmallIntegerField(default=0, verbose_name='Количество')
    price = models.SmallIntegerField(verbose_name='Цена')
    order = models.ForeignKey('Orders', verbose_name='Заказ', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_amount(self):
        return self.quantity * self.price

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Клиент')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Заказ № ' + str(self.id)