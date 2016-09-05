# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models
from django.utils.translation import ugettext as _
from colorful.fields import RGBColorField
from django.utils.safestring import mark_safe
from datetime import date
from sorl.thumbnail import ImageField

# Create your models here.

# Groups
class Group(models.Model):
    group = models.CharField(_(u'Группа'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.group)
    class Meta:
        verbose_name=_(u'Group')
        verbose_name_plural=_(u'Groups') 

# Semester
class Semester(models.Model):
    semester = models.CharField(_(u'Semester'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.semester)
    class Meta:
        verbose_name=_(u'Semester')
        verbose_name_plural=_(u'Semesters') 

# Students
class Student(models.Model):
    group = models.ForeignKey(Group, null=True, blank=True)
    last_name = models.CharField(_(u'Фамилия'), max_length=25, null=True, blank=True, default='')
    name = models.CharField(_(u'Имя'), max_length=25, null=True, blank=True, default='')
    patronym = models.CharField(_(u'Отчество'), max_length=25, null=True, blank=True, default='')
    tel = models.CharField(_(u'Номер телефона'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
  #      return '%s  (%s)' % (self.structure,self.fuel_moisture)
        return '%s' % (self.name)
    class Meta:
        verbose_name=_(u'Student')
        verbose_name_plural=_(u'Students')

# Subject names 
class Subject(models.Model):
    group = models.ManyToManyField(Group, null=True, blank=True)
    subject = models.CharField(_(u'Subject'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.subject)
    class Meta:
        verbose_name=_(u'Subject')
        verbose_name_plural=_(u'Subjects') 

# Courseworks topics
class Coursework(models.Model):
    subject = models.ForeignKey(Subject, null=True, blank=True)
    student = models.ForeignKey(Student, null=True, blank=True)
    semester = models.ForeignKey(Semester, null=True, blank=True)
    coursework = models.CharField(_(u'Subject'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.coursework)
    class Meta:
        verbose_name=_(u'Coursework')
        verbose_name_plural=_(u'Courseworks') 

# Lab topics
class Lab(models.Model):
    subject = models.ForeignKey(Subject, null=True, blank=True)
    lab = models.CharField(_(u'Subject'), max_length=3, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.lab)
    class Meta:
        verbose_name=_(u'Lab')
        verbose_name_plural=_(u'Labs') 

# Subject type (lecture, lab)
class Subject_type(models.Model):
    subject_type = models.CharField(_(u'Subject type'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.subject_type)
    class Meta:
        verbose_name=_(u'Subject type')
        verbose_name_plural=_(u'Subject types') 

# Students' progress
class Progress(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True)
    semester = models.ForeignKey(Semester, null=True, blank=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    lab = models.ForeignKey(Lab, null=True, blank=True)
    progress = models.CharField(_(u'Subject'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.pregress)
    class Meta:
        verbose_name=_(u'Progress')
        verbose_name_plural=_(u'Progress') 

# Students' absence
class Absence(models.Model):
    student = models.ForeignKey(Student, null=True, blank=True)
    semester = models.ForeignKey(Semester, null=True, blank=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True)
    subject_type = models.ForeignKey(Subject_type, null=True, blank=True)
    progress = models.CharField(_(u'Subject'), max_length=25, null=True, blank=True, default='')
    def __unicode__(self):
        return '%s' % (self.absence)
    class Meta:
        verbose_name=_(u'Absence')
        verbose_name_plural=_(u'Absence') 


