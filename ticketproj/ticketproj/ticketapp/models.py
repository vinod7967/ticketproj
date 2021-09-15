from django.db import models
class EmployeeModel(models.Model):
    Query = models.CharField(max_length=500)
    username = models.CharField(max_length=50)
    def __str__(self):
        return self.Query
class AdminModel(models.Model):
    query = models.OneToOneField(EmployeeModel,on_delete=models.CASCADE)
    ch = [('not resolved','not resolved'),('resolved','resolved')]
    status = models.CharField(max_length=50,choices=ch,default='2')
    def __str__(self):
        return self.query

