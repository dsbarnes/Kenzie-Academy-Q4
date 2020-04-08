from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=40)
    website = models.URLField(max_length=200)


class ShoeType(models.Model):
    def __str__(self):
        return self.style

    style = models.CharField(max_length=10, choices=[])


class ShoeColor(models.Model):
    def __str__(self):
        return self.color_name

    # color_enum = [
    #     ('r', 'red'),
    #     ('o', 'orange'),
    #     ('y', 'yellow'),
    #     ('g', 'green'),
    #     ('b', 'blue'),
    #     ('i', 'indigo'),
    #     ('v', 'violet'),
    #     ('k', 'black'),
    #     ('w', 'white'),
    # ]
    color_name = models.CharField( max_length=3, choices=[] )


class Shoe(models.Model):
    def __str__(self):
        return str(self.brand_name) + ' ' + str(self.shoe_type)

    size = models.IntegerField()
    brand_name = models.CharField(max_length=40)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=40)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=40)

