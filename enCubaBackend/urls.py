from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework import routers

from auth.views import GoogleLogin, FacebookLogin
from place.views import PlaceViewSet
from review.views import ReviewViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'places', PlaceViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
