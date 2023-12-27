from django.db import models

# Create your models here.

JOB_TYPE = [
    ("FT","Full Time"),
    ("PT","Part Time")
]

class Job(models.Model): 
    title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    responsibility = models.TextField(max_length=1500)
    qualification = models.TextField(max_length=1000)
    benefit = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default= 1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.title