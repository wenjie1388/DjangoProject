from django.db import models
from users.models import AbstractUser
import os

from utils.utils import get_RandomString



def course_img_path(instance, filename):
    ext = filename.split('.').pop()
    return 'course/{0}/{1}.{2}'.format(instance.user_id,get_RandomString(24), ext)
    # return 'course/{0}/{1}'.format(get_randomStr(24), filename)

# 课程信息表
class Course(models.Model):
    img = models.ImageField(
      upload_to=course_img_path,
      help_text='课程宣传封面',
      default='course/default.png'
    )
    name = models.CharField(
        help_text='课程标题',
        max_length=50,
    )
    user = models.ForeignKey(
        AbstractUser,
        on_delete=models.CASCADE,
    )

    students = models.IntegerField(
        help_text='学习人数',
        default=0,
        blank=True,
    )

    href = models.CharField(
        help_text='课程外链',
        max_length=255,
    )
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        help_text="课程价格", 
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='创建时间',      
    )


    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'course'
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        ordering = ['user_id', 'id', 'created']
