from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from gradeBookSystem.models import Course, StudentEnrollment, Semester, Lecturer, Student, Class
from gradeBookSystem.permissions import IsAuthorOrReadOnly
from gradeBookSystem.serializers import CourseSerializer, SemesterSerializer, LecturerSerializer, StudentSerializer, \
    ClassSerializer, StudentEnrollmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def list(self, request, *args, **kwargs):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        course.delete()
        return Response(status=204)

class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows semesters to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def list(self, request, *args, **kwargs):
        queryset = Semester.objects.all()
        serializer = SemesterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = SemesterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Semester.objects.all()
        semester = get_object_or_404(queryset, pk=pk)
        serializer = SemesterSerializer(semester)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Semester.objects.all()
        semester = get_object_or_404(queryset, pk=pk)
        serializer = SemesterSerializer(semester, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Semester.objects.all()
        semester = get_object_or_404(queryset, pk=pk)
        semester.delete()
        return Response(status=204)

class LecturerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows lecturers to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def list(self, request, *args, **kwargs):
            queryset = Lecturer.objects.all()
            serializer = LecturerSerializer(queryset, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = LecturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        serializer = LecturerSerializer(lecturer)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        serializer = LecturerSerializer(lecturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Lecturer.objects.all()
        lecturer = get_object_or_404(queryset, pk=pk)
        lecturer.delete()
        return Response(status=204)

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def list(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        student.delete()
        return Response(status=204)

class ClassViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows classes to be viewed or edited.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = Class.objects.all()
        serializer = ClassSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Class.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = ClassSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Class.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = ClassSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = Class.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        course.delete()
        return Response(status=204)

class StudentEnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows student enrollments to be viewed or edited.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    def list(self, request, *args, **kwargs):
        queryset = StudentEnrollment.objects.all()
        serializer = StudentEnrollmentSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StudentEnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = StudentEnrollment.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = StudentEnrollmentSerializer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = StudentEnrollment.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = StudentEnrollmentSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        queryset = StudentEnrollment.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        course.delete()
        return Response(status=204)