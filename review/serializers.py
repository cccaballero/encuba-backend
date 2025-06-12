from rest_framework.serializers import ModelSerializer

from review.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'place', 'body', 'like', 'created_at', 'updated_at', 'created_by', 'updated_by')
        read_only_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
