from rest_framework.serializers import ReadOnlyField
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from place.models import Place


class PlaceSerializer(GeoFeatureModelSerializer):

    category = ReadOnlyField()

    class Meta:
        model = Place
        geo_field = "location"
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
        extra_kwargs = {
            'location': {'required': True},
        }
