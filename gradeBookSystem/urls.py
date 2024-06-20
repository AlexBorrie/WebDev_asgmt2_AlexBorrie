from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('classes', ClassViewSet, basename='classes')
router.register('courses', CourseViewSet, basename='courses')
router.register('students', StudentViewSet, basename='students')
router.register('studentenrollments', StudentEnrollmentViewSet, basename='studentenrollments')
router.register('lecturers', LecturerViewSet, basename='lecturers')
router.register('semesters', SemesterViewSet, basename='semesters')

urlpatterns = [
    path('', include(router.urls))
]