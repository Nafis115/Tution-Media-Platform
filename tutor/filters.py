from django_filters import rest_framework as filters
from .models import TutorModel  
from django.db.models import Q

class TutorFilter(filters.FilterSet):  
    preferred_class = filters.CharFilter(method='filter_preferred_class')
    preferred_subjects = filters.CharFilter(method='filter_preferred_subjects')
    preferred_area_to_teach = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = TutorModel  
        fields = ['preferred_class', 'preferred_subjects', 'preferred_area_to_teach']

    def filter_preferred_class(self, queryset, name, value):
        class_values = value.split(',')
        return queryset.filter(preferred_class__in=class_values)

    def filter_preferred_subjects(self, queryset, name, value):
        subject_values = value.split(',')
        return queryset.filter(preferred_subjects__in=subject_values)
