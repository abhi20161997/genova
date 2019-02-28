from django.contrib import admin

from .models import Tablet,Injection,Medicine

admin.site.register(Tablet)
admin.site.register(Injection)
admin.site.register(Medicine)