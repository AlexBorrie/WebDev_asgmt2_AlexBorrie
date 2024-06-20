from rest_framework import viewsets

from gradeBookSystem.models import Course
from gradeBookSystem.serializers import CourseSerializer, SemesterSerializer, LecturerSerializer, StudentSerializer, \
    ClassSerializer, StudentEnrollmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows semesters to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = SemesterSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lecturers to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = LecturerSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = StudentSerializer

class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classes to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = ClassSerializer

class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows student enrollments to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = StudentEnrollmentSerializer