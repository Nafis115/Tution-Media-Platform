# permissions.py

from rest_framework import permissions
from tutor.models import TutorModel  # Import your Tutor model

class IsTutor(permissions.BasePermission):
    """
    Custom permission to only allow tutors to apply for tuitions.
    """

    def has_permission(self, request, view):
        # Check if the user is authenticated as a tutor
        return request.user.is_authenticated and hasattr(request.user, 'tutormodel')
