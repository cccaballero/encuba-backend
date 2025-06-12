from crum import get_current_user
from django.db import models


class BlamableModel(models.Model):
    created_by = models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey('auth.User', related_name='%(class)s_updated_by', blank=True, null=True,
                                   default=None, on_delete=models.SET_NULL)

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


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
