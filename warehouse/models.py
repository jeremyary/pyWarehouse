from django.db import models
from datetime import datetime

class Classification(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Worker(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    start_date = models.DateTimeField('employment date', default=datetime.now)
    age = models.IntegerField(default=0)
    classifications = models.ManyToManyField(Classification, blank=True)

    def __str__(self):
        return ''.join((self.last_name, ', ', self.first_name))

class Order(models.Model):
    item = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    placed = models.DateTimeField('order placed', default=datetime.now)
    status = models.CharField(max_length=25, default="placed")
    classifications = models.ManyToManyField(Classification, blank=True)
    result_id = models.CharField(max_length=60, default = '')

    def __str__(self):
        return ''.join([
                       str(self.quantity), ' of ', self.item,
                       ', time[', self.placed.strftime("%Y-%m-%d %H:%M:%S"), ']',
                       ', result_id[', self.result_id, ']',
                       ', status[', self.status, ']'
       ])




