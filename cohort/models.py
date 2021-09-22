from django.db import models


# Create your models here.
class Cohort(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Native(models.Model):
    cohort = models.OneToOneField(Cohort, on_delete=models.DO_NOTHING)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(default="", upload_to="uploads/")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
