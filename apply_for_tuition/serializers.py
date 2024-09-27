from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    tuition_title = serializers.SerializerMethodField()
    fee=serializers.SerializerMethodField()
    applicant_name=serializers.SerializerMethodField()

    def get_tuition_title(self, obj):
        return obj.tuition.title
    def get_fee(self, obj):
        return obj.tuition.salary
    def get_applicant_name(self, obj):
        return f"{obj.tutor.user.first_name} {obj.tutor.user.last_name}"

    class Meta:
        model = Application
        fields = ['id', 'tutor', 'tuition','fee', 'tuition_title', 'applicant_name', 'status', 'message']