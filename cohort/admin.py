from django.contrib import admin

# Register your models here.
from cohort.models import Cohort, Native

admin.site.register(Cohort)
admin.site.register(Native)
