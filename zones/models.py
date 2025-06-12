from crum import get_current_user
from django.contrib.gis.db import models

from place.models import Place


class Zone(models.Model):
    name = models.CharField(max_length=255)
    boundaries = models.GeometryField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey('auth.User', related_name='%(class)s_updated_by', blank=True, null=True,
                                   default=None, on_delete=models.SET_NULL)

    def get_places(self):
       return  self.get_places_query().all()

    def get_places_query(self):
        return Place.objects.filter(location__contained=self.boundaries)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

class Province(Zone):

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

class Municipality(Zone):

    class Meta:
        verbose_name = "Municipality"
        verbose_name_plural = "Municipalities"
