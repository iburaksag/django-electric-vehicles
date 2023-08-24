from django.contrib import admin
from .models import EV 


class EVAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'manufacturer', 'battery_size', 'wltp_range', 'cost', 'power']    


admin.site.register(EV, EVAdmin)