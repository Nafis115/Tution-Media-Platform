from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    tuition_title = serializers.SerializerMethodField()

    def get_tuition_title(self, obj):
        return obj.tuition.title

    class Meta:
        model = Application
        fields = ['id', 'tutor', 'tuition', 'tuition_title', 'status', 'message']