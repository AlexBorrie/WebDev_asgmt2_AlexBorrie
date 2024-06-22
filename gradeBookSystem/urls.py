from django.db.models import Index
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gradeBookSystem.viewsets import ClassViewSet, CourseViewSet, StudentViewSet, StudentEnrollmentViewSet, \
    LecturerViewSet, SemesterViewSet

router = DefaultRouter()
router.register('classes', ClassViewSet, basename='classes')
router.register('courses', CourseViewSet, basename='courses')
router.register('students', StudentViewSet, basename='students')
router.register('studentenrollments', StudentEnrollmentViewSet, basename='studentenrollments')
router.register('lecturers', LecturerViewSet, basename='lecturers')
router.register('semesters', SemesterViewSet, basename='semesters')

urlpatterns = [
    path('', Index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]