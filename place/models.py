from crum import get_current_user
from django.contrib.gis.db import models
from django.utils.text import slugify


class Place(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, default=None)
    description = models.TextField(default=None, null=True, blank=True)
    address = models.CharField(max_length=255)
    location = models.PointField()
    amenity = models.CharField(max_length=255, default=None, null=True, blank=True)
    tourism = models.CharField(max_length=255, default=None, null=True, blank=True)
    office = models.CharField(max_length=255, default=None, null=True, blank=True)
    phone = models.CharField(max_length=255, default=None, null=True, blank=True)
    email = models.CharField(max_length=255, default=None, null=True, blank=True)
    website = models.CharField(max_length=255, default=None, null=True, blank=True)
    facebook = models.CharField(max_length=255, default=None, null=True, blank=True)
    twitter = models.CharField(max_length=255, default=None, null=True, blank=True)
    instagram = models.CharField(max_length=255, default=None, null=True, blank=True)
    linkedin = models.CharField(max_length=255, default=None, null=True, blank=True)
    youtube = models.CharField(max_length=255, default=None, null=True, blank=True)
    google = models.CharField(max_length=255, default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, default=None, on_delete=models.SET_NULL)
    updated_by = models.ForeignKey('auth.User', related_name='%(class)s_updated_by', blank=True, null=True,
                                   default=None, on_delete=models.SET_NULL)

    @property
    def category(self):
        return self.amenity or self.tourism or self.office

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Place"
        verbose_name_plural = "Places"