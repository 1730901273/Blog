# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import VmaigUser
from .forms import VmaigUserCreationForm


# Register your models here.

class VmaigUserAdmin(UserAdmin):
    add_form = VmaigUserCreationForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')
        }),
    )
    fieldsets = (
        (u'基本信息', dict(fields=('username', 'password', 'email', 'img', 'intro'))),
        (u'权限', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (u'时间信息', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.unregister(Group)
admin.site.register(VmaigUser, VmaigUserAdmin)
# 修改网页title和站点header。
admin.site.site_title = "Vblog后台管理"
admin.site.site_header = "Vblog"
