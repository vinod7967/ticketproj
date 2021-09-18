from django.db import models

class EmployeeModel(models.Model):
    Query = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    ch = [('not resolved', 'not resolved'), ('resolved', 'resolved')]
    status = models.CharField(max_length=50, choices=ch, default='Not resolved')
    def __str__(self):
        return self.Query

