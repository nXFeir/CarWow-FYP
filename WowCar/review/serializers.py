from rest_framework import serializers

from .models import *

class ReviewSerializer(serializers.ModelSerializer):
    comments = serializers.PrimaryKeyRelatedField(many=True, queryset=Comment.objects.all(), required=False)
    class Meta:
        model = Review
        fields = ['id', 'car_model', 'reviewer', 'score', 'content', 'comments', 'created_at']

    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields["car_model"].read_only = True
            fields["reviewer"].read_only = True
        return fields


class CommentSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(required=True)
    class Meta:
        model = Comment
        fields = ['id', 'review', 'commenter', 'comment', 'created_at']

    def get_fields(self):
        fields = super().get_fields()
        if self.instance:
            fields["review"].read_only = True
            fields["commenter"].read_only = True
        return fields