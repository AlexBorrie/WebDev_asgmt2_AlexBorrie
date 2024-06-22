import password
from rest_framework import serializers

from gradeBookSystem.models import Course, Semester, Lecturer, Student, StudentEnrollment, Class


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'code']

        extra_kwargs = {
            password: {
                'write_only': True,
                'required': True
            }

        }

        def create(self, validated_data):
            return Course.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.name = validated_data.get('name', instance.name)
            instance.code = validated_data.get('code', instance.code)
            instance.save()
            return instance

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['id', 'year', 'semester']

        def create(self, validated_data):
            return Semester.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.year = validated_data.get('year', instance.year)
            instance.semester = validated_data.get('semester', instance.semester)
            instance.save()
            return instance

class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['id', 'firstName', 'lastName', 'email', 'DOB']

        extra_kwargs = {
            password: {
                'write_only': True,
                'required': True
            }

        }

        def create(self, validated_data):
            return Lecturer.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.firstName = validated_data.get('firstName', instance.firstName)
            instance.lastName = validated_data.get('lastName', instance.lastName)
            instance.email = validated_data.get('email', instance.email)
            instance.DOB = validated_data.get('DOB', instance.DOB)
            instance.save()
            return instance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'firstName', 'lastName', 'email', 'DOB', 'course', 'semester']

        extra_kwargs = {
            password: {
                'write_only': True,
                'required': True
            }

        }

        def create(self, validated_data):
            return Student.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.firstName = validated_data.get('firstName', instance.firstName)
            instance.lastName = validated_data.get('lastName', instance.lastName)
            instance.email = validated_data.get('email', instance.email)
            instance.DOB = validated_data.get('DOB', instance.DOB)
            instance.course = validated_data.get('course', instance.course)
            instance.semester = validated_data.get('semester', instance.semester)
            instance.save()
            return instance

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'number', 'course', 'semester', 'lecturer']

        extra_kwargs = {
            password: {
                'write_only': True,
                'required': True
            }

        }

        def create(self, validated_data):
            return Class.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.number = validated_data.get('number', instance.number)
            instance.course = validated_data.get('course', instance.course)
            instance.semester = validated_data.get('semester', instance.semester)
            instance.lecturer = validated_data.get('lecturer', instance.lecturer)
            instance.save()
            return instance
class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = ['id', 'studentID', 'classID', 'grade', 'enrollmentDate', 'gradeDate']

        extra_kwargs = {
            password: {
                'write_only': True,
                'required': True
            }

        }

        def create(self, validated_data):
            return StudentEnrollment.objects.create(**validated_data)

        def update(self, instance, validated_data):
            instance.studentID = validated_data.get('studentID', instance.studentID)
            instance.classID = validated_data.get('classID', instance.classID)
            instance.grade = validated_data.get('grade', instance.grade)
            instance.enrollmentDate = validated_data.get('enrollmentDate', instance.enrollmentDate)
            instance.gradeDate = validated_data.get('gradeDate', instance.gradeDate)
            instance.save()
            return instance