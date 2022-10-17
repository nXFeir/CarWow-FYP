from rest_framework import serializers

from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'car_model', 'reviewer', 'score', 'content', 'created_at']

    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields["car_model"].read_only = True
            fields["reviewer"].read_only = True
        return fields