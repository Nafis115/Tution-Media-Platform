from django_filters import rest_framework as filters
from .models import Tuition

class TuitionFilter(filters.FilterSet):
    subjects = filters.CharFilter(field_name='subjects__in', lookup_expr='in')
    tuition_class = filters.CharFilter(lookup_expr='exact')

    class Meta:
        model = Tuition
        fields = ['subjects', 'tuition_class']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['subjects'].extra.update({'required': False})
        self.filters['tuition_class'].extra.update({'required': False})
