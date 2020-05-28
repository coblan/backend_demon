from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
from django.contrib.auth.models import User
# Create your models here.
class TBDepartment(models.Model):
    name = models.CharField('部门名称',max_length =200)
    leader = models.CharField('领导',max_length=100,blank=True)
    parent = models.ForeignKey('TBDepartment',verbose_name = '上级部门',related_name='children',null=True,blank=True)
    path = models.CharField('路径',max_length=100,blank=True)
    
    def __str__(self):
        return self.name
    
GEN_TYPE=(
    (0,'未知'),
    (1,'男'),
    (2,'女')
)
class TBEmployee(models.Model):
    name = models.CharField('员工姓名',max_length=100)
    no = models.CharField('工号',max_length =100,blank=True)
    gen = models.IntegerField(verbose_name='性别',default=0,choices=GEN_TYPE)
    mobile = models.CharField('手机号',max_length=30,blank=True)
    head = PictureField('工牌照',max_length=200,blank=True)
    depart = models.ForeignKey(TBDepartment,null=True,blank=True,verbose_name='部门')
    user = models.OneToOneField(User,verbose_name = '账号',null=True,blank=True)
    duty = models.CharField('职务',max_length = 100,blank=True)
    nation = models.CharField('民族',max_length = 30 ,blank=True)
    birthday = models.DateField('生日',null=True,blank=True)
    nickname = models.CharField('个性签名',max_length = 200,blank=True)
    qq = models.CharField('QQ',max_length = 50,blank=True)
    
    
    def __str__(self):
        return self.name
