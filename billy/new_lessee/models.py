from django.db import models

# Create your models here.
class Lessee(models.Model):
    complex = models.CharField(max_length=255)
    num_contract = models.CharField(max_length=255)
    data1= models.DateField(auto_now_add=True)
    data2= models.DateField(auto_now_add=True)
    data3= models.DateField(auto_now_add=True)
    lessee = models.CharField(max_length=255)
    lessor = models.CharField(max_length=255)
    lessor_r_s = models.CharField(max_length=255)
    # checbox1 = models.CheckConstraint(blank=True,null=True) 
    # checbox2 = models.CheckConstraint(blank=True,null=True) 
    # checbox3 = models.CheckConstraint(blank=True,null=True) 
    type_contract = models.CharField(max_length=255)
    comment = models.TextField()
    num_document_in_count = models.CharField(max_length=255)
    main_contract = models.CharField(max_length=255)
    main_lot = models.IntegerField()