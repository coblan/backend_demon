from django.db import models
from helpers.director.model_func.cus_fields.cus_picture import PictureField
# Create your models here.

IMAGE_STATUS=(
    (0,'未发布'),
    (1,'在线'),
    (2,'下线')
)
    
class SourceImage(models.Model):
    tag_content = models.CharField('标签',max_length=300,blank=True)
    status = models.IntegerField('状态',default=0,choices=IMAGE_STATUS)
    url = PictureField('图片',max_length=200,blank=True)
    color_block = PictureField('色块',max_length=200,blank=True)
    thumbnail = PictureField('缩略图',max_length=200,blank=True)
    uploadtime = models.DateTimeField('上传日期',null=True,blank=True)
    resolution = models.CharField('分辨率',max_length=30,blank=True)
    size = models.CharField('大小',max_length=30,blank=True)
  
    def __str__(self):
        return str(self.id )

class Tag(models.Model):
    content = models.CharField('内容',max_length=50)
    
    def __str__(self):
        return self.content or '标签'
    
PALETTE_KIND=(
    (0,'纯色'),
    (1,'过渡色'),
)

class Palette(models.Model):
    zh = models.CharField('中文名', max_length=200)
    en = models.CharField('英文名',max_length=200,blank=True)
    colors = models.TextField('颜色盘',blank=True)
    kind = models.IntegerField('颜色种类',default=0,choices=PALETTE_KIND)
    
    def __str__(self):
        return self.zh or '色盘'

class ImageGroup(models.Model):
    zh = models.CharField('中文名',max_length=200,)
    en = models.CharField('英文名',max_length=200,blank=True)
    status = models.IntegerField('状态',default=0,choices=IMAGE_STATUS)
    images = models.ManyToManyField(SourceImage,verbose_name='图片')
    cover = PictureField('图片',max_length=200,blank=True)
    
    def __str__(self):
        return self.zh
    

class WechatShare(models.Model):
    image = models.ForeignKey(SourceImage,verbose_name='图片')
    ip = models.CharField('ip',max_length=30)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now=True)

IMAGE_REPORT_CODE = (
    (1,'打开'),
    (2,'关闭'),
)

class ImageReport(models.Model):
    image = models.ForeignKey(SourceImage,verbose_name='图片')
    ip = models.CharField('ip',max_length=30)
    createtime = models.DateTimeField(verbose_name='创建时间',auto_now=True)
    code = models.IntegerField(verbose_name='编码',choices=IMAGE_REPORT_CODE)