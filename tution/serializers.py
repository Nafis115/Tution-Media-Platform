from rest_framework import serializers
from .models import Tuition

class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = '__all__'