from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from zones.models import Municipality, Province

# Register your models here.
admin.site.register(Municipality, OSMGeoAdmin)
admin.site.register(Province, OSMGeoAdmin)
