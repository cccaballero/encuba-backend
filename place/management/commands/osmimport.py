import math

import osmnx
import pandas
from django.contrib.gis.geos import Point
from django.core.management.base import BaseCommand, CommandError

from place.models import Place


# from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Import data from OSM'

    # place = 'Cuba'
    # place = 'Cienfuegos, Cienfuegos, Cuba'
    place = 'Habana, Cuba'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('okokok'))

        Place.objects.all().delete()

        tags = {
            'amenity': [
                'grave_yard',
                'courthouse',
                'embassy',
                'police',
                'mortuary',
                'bar',
                'pub',
                'fast_food',
                'cafe',
                'ice_cream',
                'restaurant',
            ],
            'tourism': [
                'guest_house',
                'hostel',
                'hotel',
            ],
            'landuse': [
                'cemetery',
            ],
            'building': [
                'government',
            ],
            'office': [
                'government',
            ],
        }
        places = osmnx.geometries_from_place(self.place, tags=tags)
        places_points = places[places.geom_type == 'Point']

        places_iter = places_points.iterrows()
        for index, place in places_iter:
            name = self._get_from_data(place, 'name')
            if not name:
                continue
            location = Point(place.get('geometry').x, place.get('geometry').y)
            amenity = self._get_from_data(place, 'amenity')
            tourism = self._get_from_data(place, 'tourism')
            office = self._get_from_data(place, 'office')
            phone = self._get_from_data(place, 'phone')
            email = self._get_from_data(place, 'contact:email')
            website = self._get_from_data(place, 'website')
            facebook = self._get_from_data(place, 'contact:facebook')
            twitter = self._get_from_data(place, 'contact:twitter')
            instagram = self._get_from_data(place, 'contact:instagram')
            linkedin = self._get_from_data(place, 'contact:linkedin')
            youtube = self._get_from_data(place, 'contact:youtube')
            google = self._get_from_data(place, 'contact:google')

            Place.objects.create(
                name=name,
                location=location,
                amenity=amenity,
                tourism=tourism,
                office=office,
                phone=phone,
                email=email,
                website=website,
                facebook=facebook,
                twitter=twitter,
                instagram=instagram,
                linkedin=linkedin,
                youtube=youtube,
                google=google,
            )

    def _get_from_data(self, data, key):
        value = data.get(key, None)
        return value if value and not pandas.isna(value) else ''
