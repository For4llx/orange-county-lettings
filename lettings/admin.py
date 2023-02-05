from django.contrib import admin
from .models import Letting, Address

admin.site.register([Letting, Address])
