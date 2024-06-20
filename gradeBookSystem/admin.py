from django.contrib import admin

# Register your models here.
from .models import Class, Course, Student, StudentEnrollment, Lecturer, Semester

admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentEnrollment)
admin.site.register(Lecturer)
admin.site.register(Semester)
