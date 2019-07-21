from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()
	teacher = models.ForeignKey(User, on_delete=models.CASCADE)


class Student(models.Model):
	Gender = (
	("Male", "Male"),
	("Female", "Female"),
)
	Grade = (
	("A", "A"),
	("B", "B"),
	("C", "C"),
	("D", "D"),
	("F", "F"),
	("S", "S"),
)
	name = models.CharField(max_length=120)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=9, choices=Gender, default='Male')
	exam_grade = models.CharField(max_length=1, choices=Grade, default='A')
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)


	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})
