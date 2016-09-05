# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from mystudents.models import Student, Group
from django.conf import settings


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group',)
    search_fields = ('group',)
    list_filter = ('group',) 

admin.site.register(Group, GroupAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('group', 'last_name', 'name', 'patronym', 'tel',)
    search_fields = ('group', 'last_name', 'name', 'patronym', 'tel',)
    list_filter = ('group', 'last_name', 'name', 'patronym', 'tel',) 

admin.site.register(Student, StudentAdmin)
