from django import db
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import CharField
from apps.students.models import Student
from config.constants import APPLIED_BY, APPLICATIONS_STATUS, JOB_PORTAL
# Create your models here.


class Application(models.Model):
    class Meta(object):
        db_table = 'Application'


student = models.ForeignKey(
    Student, on_delete=CASCADE, db_index=True
)
applied_admin_id = models.IntegerField(
    'Applied Admin_ID', blank=True, null=True, db_index=True
)
applied_by = models.CharField(
    'Applied By', blank=False, null=False, choices=APPLIED_BY, max_length=50, db_index=True
)
application_status = models.CharField(
    'Application Status', blank=False, null=False, max_length=50, choices=APPLICATIONS_STATUS, db_index=True
)
company_name = models.CharField(
    'Company Name', blank=False, null=False, max_length=50, db_index=True
)
position = models.CharField(
    'Position', blank=False, null=False, max_length=50, db_index=True
)
job_description = models.TextField(
    'Job Description', blank=True, null=True, max_length=100
)
job_post_url = models.URLField(
    'Job Post URL', blank=True, null=True
)
state = models.CharField(
    'State', blank=False, null=False, max_length=50, db_index=True
)
note = models.TextField(
    'Note', blank=True, null=True, max_length=100, db_index=True
)
job_portal = models.CharField(
    'Job Portal', blank=False, null=False, choices=JOB_PORTAL, db_index=True
)
created = models.DateTimeField(
    'Created at', blank=False, null=False, auto_now_add=True
)
updated = models.DateTimeField(
    'Updated at', blank=False, null=False, auto_now=True
)
