from django.db import models

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField()
    semester = models.CharField(max_length=10)

    def __str__(self):
        return self.semester

class Lecturer(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    DOB = models.DateField()



class Student(models.Model):
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    DOB = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class StudentEnrollment(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    classID = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.IntegerField()
    enrollmentDate = models.DateField()
    gradeDate = models.DateField()
