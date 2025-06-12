from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin

from place.models import Place


class PlaceAdmin(OSMGeoAdmin):
    search_fields = (
        "id",
        "name",
    )
admin.site.register(Place, PlaceAdmin)
