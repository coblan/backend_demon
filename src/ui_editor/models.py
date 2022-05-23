from django.db import models

# Create your models here.

class Page(models.Model):
    name = models.CharField('名称',max_length=50,primary_key=True)
    content = models.TextField('内容',blank=True)
    
    
