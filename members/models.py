from django.db import models

# Create your models here.
class Task(models.Model):
    title= models.CharField(max_length=35)
    description= models.TextField(null=True,blank=True)
    due_Date= models.DateField()
    due_time= models.TimeField()
    completed =models.BooleanField(default=False)
     
    def __str__(self)->str:
      return super().__str__()
       
       