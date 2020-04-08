from django.contrib import admin
from api.models import Manufacturer, ShoeType, ShoeColor, Shoe

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(ShoeType)
admin.site.register(ShoeColor)
admin.site.register(Shoe)
