from django.db import models

# Create your models here.
class prebooking(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=50)
    Mobile_no = models.CharField(max_length=15)
    Email_id= models.EmailField()
    Trip_start_date = models.DateField(null=True)
    Trip_end_date = models.DateField(null=True)
    Your_State = models.CharField(max_length=50)
    Your_District = models.CharField(max_length=50)
    Distination = models.CharField(max_length=50)
    Members_in_Trip = models.IntegerField()
    Adults_in_Trip = models.IntegerField()
    Childerns_in_Trip = models.IntegerField()
