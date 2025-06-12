from django.db.models import Q
# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter, BaseFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_gis.filters import InBBoxFilter, TMSTileFilter, DistanceToPointFilter
from rest_framework_gis.pagination import GeoJsonPagination

from place.models import Place
from place.permissions import IsPlaceOwnerOrReadOnly
from place.serializers import PlaceSerializer
from zones.models import Municipality, Province


class StandardPlaceSetPagination(GeoJsonPagination):
    page_size = 50
    # page_size_query_param = 'page_size'
    # max_page_size = 1000


class MunicipalityFilter(BaseFilterBackend):
    """
    Filter places by municipality.
    """

    def filter_queryset(self, request, queryset, view):
        municipality_str = request.query_params.get('municipality', None)
        if municipality_str is None:
            return queryset
        municipality = None
        if municipality_str.isnumeric():
            municipality = Municipality.objects.filter(id=municipality_str).first()
        elif municipality_str:
            municipality = Municipality.objects.filter(name__iexact=municipality_str).first()
        if not municipality:
            return queryset.filter(id=0)
        return queryset.filter(location__contained=municipality.boundaries)


class ProvinceFilter(BaseFilterBackend):
    """
    Filter places by province.
    """

    def filter_queryset(self, request, queryset, view):
        province_str = request.query_params.get('province', None)
        if province_str is None:
            return queryset
        province = None
        if province_str.isnumeric():
            province = Province.objects.filter(id=province_str).first()
        elif province_str:
            province = Province.objects.filter(name__iexact=province_str).first()
        if not province:
            queryset.filter(id=0)
        return queryset.filter(location__contained=province.boundaries)


class CategoryFilter(BaseFilterBackend):
    """
    Filter places by category.
    """

    def filter_queryset(self, request, queryset, view):
        category_str = request.query_params.get('category', None)
        if category_str is None:
            return queryset
        return queryset.filter(Q(amenity=category_str) | Q(tourism=category_str) | Q(office=category_str))


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows places to be viewed or edited.
    """
    queryset = Place.objects.all().order_by('-created_at')
    serializer_class = PlaceSerializer

    pagination_class = StandardPlaceSetPagination

    filter_backends = (CategoryFilter, ProvinceFilter, MunicipalityFilter, SearchFilter, InBBoxFilter, TMSTileFilter,
                       DistanceToPointFilter,)
    search_fields = ('name', 'description',)
    bbox_filter_field = 'location'
    bbox_filter_include_overlapping = True
    distance_filter_field = 'location'

    permission_classes = [IsAuthenticatedOrReadOnly, IsPlaceOwnerOrReadOnly]
