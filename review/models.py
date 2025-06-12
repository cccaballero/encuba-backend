from django.db import models
from django.db.models import Model, CASCADE
from django.utils.translation import gettext_lazy as _

from common.models import BlamableModel, TimestampModel


class Review(BlamableModel, TimestampModel):
    place = models.ForeignKey('place.Place', on_delete=CASCADE, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    like = models.BooleanField(blank=False)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
