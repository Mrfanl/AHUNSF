from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='昵称')
#     nickname = models.CharField(max_length=20)
#
#     def __str__(self):
#         return '<Profile: %s for %s>' % (self.nickname, self.user.username)


class Follow(models.Model):
    # 两个相同的外键，通过related_name区分,Follow.idol.all()和Follow.fans.all()获取
    idol = models.ForeignKey(User, on_delete=models.CASCADE, related_name='idol')
    fans = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fans')
    followTime = models.DateTimeField(auto_now_add=True)  # 自动设置添加时间