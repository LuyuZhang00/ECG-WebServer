from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class PatientManage(models.Model):

    # objects = None
    sex_choices=[
        ("0", "女性"),
        ("1","男性"),
    ]
    patient_id = models.IntegerField(verbose_name="患者编号", unique=True)
    patient_name = models.CharField(verbose_name="患者姓名", max_length=65)
    patient_age = models.SmallIntegerField(verbose_name="患者年龄", null=True, blank=True,
                                           validators=[
                                               MinValueValidator(0),
                                               MaxValueValidator(150),
                                           ])
    # patient_sex= models.BinaryField(verbose_name="患者性别", choices=sex_choices)
    patient_sex = models.CharField(verbose_name="患者性别", choices=sex_choices, null=True, blank=True, max_length=2)

    patient_department = models.CharField(verbose_name="检测类型", max_length=60,default="心电")
    patient_describe = RichTextUploadingField(verbose_name="检测描述", max_length=200)
    patient_photo = models.FileField(verbose_name="诊断影片", null=True,blank=True, upload_to='static/patient/%Y/%m/%d/')
    patient_telephone= models.CharField(verbose_name="患者电话", null=True,blank=True,max_length=11)

    create_by = models.CharField('创建人', max_length=64,default="doctor")  # 创建人
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_by = models.CharField('更新人', max_length=64,default="doctor")  # 更新人
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        # db_table=""
        verbose_name = "患者名单"
        verbose_name_plural = "患者名单"

    def __str__(self):
        return self.patient_name