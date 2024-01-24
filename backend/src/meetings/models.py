from django.db import models
from django.utils.timezone import now
from projects.models import Project


# Create your models here.
class Meeting(models.Model):
    option_1_time = models.CharField(max_length=100, null = True, default = "")
    option_2_time = models.CharField(max_length=100, null = True, default = "")

    option_3_time = models.CharField(max_length=100, null = True, default = "")

    description = models.CharField(max_length=100, null=True, default = "")
    is_accepted = models.BooleanField(default=False)
    project = models.CharField(max_length=255, default ='Project Name')
    founder = models.EmailField(max_length =255, default ='Email')
    
    invitee = models.EmailField(default= "Email")
    chosen_time = models.DateTimeField(null=True, blank=True, default= "")
    link = models.URLField(max_length=200, null=True, blank=True, default= "")
    

    def __str__(self):
        return self.project.project_name + " " + self.invitee + " " + self.founder