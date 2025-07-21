from django.db import models



class WheelSpecification(models.Model):
    condemning_dia = models.CharField(max_length=10)
    last_shop_issue_size = models.CharField(max_length=10)
    tread_diameter_new = models.CharField(max_length=10)
    wheel_gauge = models.CharField(max_length=10)
    form_number = models.CharField(max_length=50)
    submitted_by = models.CharField(max_length=100)
    submitted_date = models.DateField()

    def __str__(self):
        return self.form_number
