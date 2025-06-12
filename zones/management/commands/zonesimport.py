import json

from django.core.management.base import BaseCommand

from zones.models import Province, Municipality

class Command(BaseCommand):
    help = 'Import data from OSM'

    provinces_file = 'zones/data/provinces.geojson'
    municipalities_file = 'zones/data/municipalities.geojson'

    def handle(self, *args, **options):

        Municipality.objects.all().delete()
        Province.objects.all().delete()

        with open(self.provinces_file) as provinces:
            data = json.load(provinces)
            for feature in data['features']:
                Province.objects.create(name=feature['properties']['local_name'], boundaries=json.dumps(feature['geometry']))

        with open(self.municipalities_file) as municipalities:
            data = json.load(municipalities)
            for feature in data['features']:
                Municipality.objects.create(name=feature['properties']['local_name'], boundaries=json.dumps(feature['geometry']))
