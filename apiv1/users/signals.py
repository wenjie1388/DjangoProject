from django.conf import settings
from django.db.models.signals import post_save

from django.dispatch import receiver







@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def generate_token(sender,instance=None,created=False,**kwargs):
    ''' 创建用户时，新建 Token 
    post_save ：信号机制函数
    sender
    instance=None : AUTH_USER_MODEL 的实例
    created=False ：表示是否创建
    '''
    # if created:
      # Token.objects.create(user=instance)
    print('已创建用户')