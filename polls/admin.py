from django.contrib import admin

# Register your models here.

from . import models

# 将models 注册到后台管理上面
admin.site.register(models.Poll)
admin.site.register(models.Choice)