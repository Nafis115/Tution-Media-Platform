from rest_framework import serializers
from .models import Tuition,Review
from rest_framework import serializers
from tutor.constants import *

class TuitionSerializer(serializers.ModelSerializer):
    subject_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()
 
 

    class Meta:
        model = Tuition
        fields = '__all__'  

    def get_subject_name(self, obj):
        return [subject.name for subject in obj.subjects.all()]

    def get_author_name(self, obj):
        return f"{obj.author.user.first_name} {obj.author.user.last_name}"






class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'review', 'created_at']
   