from django.contrib import admin

# Register your models here.
from add_upd.models import req_address, req_info

admin.site.register(req_address)
admin.site.register(req_info)
