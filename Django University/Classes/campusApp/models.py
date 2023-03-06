from django.db import models


# Create your models here.

class UniversityCampus(models.Model):
    campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_State = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        display_course = '{0.campus_Name}: {0.campus_State}'
        return display_course.format(self)

    # removes added S that django adds
    class Meta:
        verbose_name_plural = "University Campus"