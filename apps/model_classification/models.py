from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class ModelManage(models.Model):
    objects = None
    model_name = models.CharField(verbose_name="模型名称", max_length=65, unique=True)
    model_file = models.FileField(verbose_name= "模型文件",upload_to='static/upload/%Y/%m/%d/',null= True,blank=True)
    model_describe = RichTextUploadingField(verbose_name="模型描述", blank=True,null=True,max_length=200)

    model_type = models.CharField(verbose_name="模型类型", max_length=65, null=True, blank=True)
    model_version = models.CharField(verbose_name="模型版本", max_length=65, null=True, blank=True)
    model_author = models.CharField(verbose_name="模型作者", max_length=65, null=True, blank=True)
    model_link= models.URLField(verbose_name="模型链接", max_length=65, null=True, blank=True)

    is_use = models.BooleanField(verbose_name="是否使用", default=False)
    is_delete = models.BooleanField(verbose_name="是否删除", default=False)

    create_by = models.CharField('创建人', max_length=64,default="root")  # 创建人
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_by = models.CharField('更新人', max_length=64,default="root")  # 更新人
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        # db_table=""
        verbose_name = "模型列表"
        verbose_name_plural = "模型列表"

    def __str__(self):
        return self.model_name