# views.py
from .models import Application
from .serializers import ApplicationSerializer
from tutor.models import TutorModel  
from rest_framework import viewsets



class ApplicationCreateView(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class =  ApplicationSerializer
    
    # custom query kortechi
    def get_queryset(self):
        queryset = super().get_queryset() # 7 no line ke niye aslam ba patient ke inherit korlam
        print(self.request.query_params)
        tutor_id = self.request.query_params.get('tutor_id')
        if tutor_id:
            queryset = queryset.filter(tutor_id=tutor_id)
        return queryset