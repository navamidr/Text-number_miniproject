from django.contrib import admin
from .models import Convert,conversion,User
# from.models import Conversion
# Register your models here.


admin.site.register(conversion)
# admin.site.register(Conversion)


admin.site.register(Convert)
admin.site.register(User)