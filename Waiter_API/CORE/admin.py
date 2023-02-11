from django.contrib import admin
from CORE.models import *

admin.site.register(Client) # < Can be changed manually by the admin
admin.site.register(Order)
admin.site.register(Menu)