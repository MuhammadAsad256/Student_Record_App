from django.db import models

class Students(models.Model):
    student_id = models.CharField(max_length=20, unique=True, primary_key=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100, blank=True, null=True)  # New field
    which_class = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    contact = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name
