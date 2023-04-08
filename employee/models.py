from django.db import models

class Employee(models.Model):
    eid = models.CharField("employee id", max_length=20, unique=True, blank=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField("phone", max_length=15)
    
    def __str__(self):
        return "%s" %(self.name)
    
    class Meta:
        db_table = 'employee'