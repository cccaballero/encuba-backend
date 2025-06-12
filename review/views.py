from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from review.models import Review
from review.permissions import IsReviewAuthorOrReadOnly
from review.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reviews to be viewed or edited.
    """
    queryset = Review.objects.all().order_by('-updated_at')
    serializer_class = ReviewSerializer

    # filter_backends = (BaseFilterBackend,)

    permission_classes = [IsAuthenticatedOrReadOnly, IsReviewAuthorOrReadOnly]
