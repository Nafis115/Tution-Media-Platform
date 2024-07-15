from rest_framework import serializers
from .models import Tuition,Review

class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    reviewer_name = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = '__all__'
    def get_reviewer_name(self, obj):
        return f"{obj.reviewer.user.first_name} {obj.reviewer.user.last_name}"