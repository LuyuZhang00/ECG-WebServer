from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
# class DoctorManage(models.Model):
#     sex_choices=[
#         ("0", "女性"),
#         ("1","男性"),
#     ]
#     doctor_id = models.IntegerField(verbose_name="医生工号", unique=True)
#     doctor_name = models.CharField(verbose_name="医生姓名", max_length=65)
#     doctor_photo = models.FileField(verbose_name="医生照片", upload_to='static/hospital/%Y/%m/%d/', null=True, blank=True)
#     doctor_age = models.SmallIntegerField(verbose_name= "医生年龄",null= True,blank=True,
#                                           validators=[
#                                               MinValueValidator(18),
#                                               MaxValueValidator(65),
#                                           ])
#     doctor_department = models.CharField(verbose_name="所属科室", max_length=60,null= True,blank=True)
#     # doctor_sex= models.BinaryField(verbose_name="医生性别", choices=sex_choices,null= True,blank=True)
#     doctor_sex= models.CharField(verbose_name="医生性别", choices=sex_choices,null= True,blank=True,max_length=2)
#
#     doctor_describe = models.TextField(verbose_name="医生介绍", max_length=200,null= True,blank=True)
#     doctor_title = models.CharField(verbose_name="医生职称", max_length=60,null= True,blank=True)
#     doctor_telephone= models.CharField(verbose_name="医生电话", max_length=11,null= True,blank=True)
#
#     create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
#     update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
#
#     class Meta:
#         # db_table=""
#         verbose_name = "医生名单"
#         verbose_name_plural = "医生名单"
#
#     def __str__(self):
#         return self.doctor_name
class HospitalManage(models.Model):

    hospital_id = models.IntegerField(verbose_name="医院编号", unique=True)
    hospital_name = models.CharField(verbose_name="医院名称", max_length=65)
    hospital_address = models.CharField(verbose_name="医院地址", null=True,blank=True,max_length=65)
    hospital_describe = RichTextUploadingField(verbose_name="医院介绍", blank=True,null=True,max_length=200)
    hospital_telephone = models.CharField(verbose_name="联系电话", blank=True,null=True,max_length=11)
    hospital_people = models.CharField(verbose_name="联系人", blank=True, null=True, max_length=11)

    hospital_SoftLicense = models.IntegerField(verbose_name="License授权总次数", default=0,validators=[
                                                    MinValueValidator(0),
                                               ])
    hospital_SoftLicense_used = models.IntegerField(verbose_name="License已使用次数", default=0,validators=[
                                                    MinValueValidator(0),
                                               ])
    create_by = models.CharField('购买人', max_length=64,default="root")  # 创建人
    create_time = models.DateTimeField(verbose_name="购买时间", auto_now_add=True)
    update_by = models.CharField('更新人', max_length=64,default="root")  # 更新人
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        # db_table=""
        verbose_name = "医院名单"
        verbose_name_plural = "医院名单"

    def __str__(self):
        return self.hospital_name