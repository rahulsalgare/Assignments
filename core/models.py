from django.db import models

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    lessons = models.ManyToManyField(Lesson)                 #considering course can have multiple lessons and lesson can belong to multiple courses.
    image = models.ImageField(upload_to='course_images/', null=True)

    def __str__(self):
        return self.title
