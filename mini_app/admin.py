from django.contrib import admin
from .models import conversion
from .models import Convert
# from.models import Conversion
# Register your models here.
admin.site.register(conversion)
# admin.site.register(Conversion)
admin.site.register(Convert)
