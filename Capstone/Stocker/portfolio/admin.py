from django.contrib import admin
from .models import Company, Holdings, Portfolio

# Register your models here.
admin.site.register(Company)
admin.site.register(Holdings)
admin.site.register(Portfolio)