from django.db.models.deletion import CASCADE
from django.db import models
from apps.students.models import Student
from apps.applications.models import Application
from config.constants import INTERVIEW_STATUS, INTERVIEW_TYPE, INTERVIEW_STUDENT_TIMEZONE

# Create your models here.


class Interview(models.Model):
    class Meta:
        db_table = 'Interview'

    student = models.ForeignKey(
        Student, on_delete=CASCADE, db_index=True
    )
    application = models.ForeignKey(
        Application, on_delete=CASCADE, db_index=True
    )
    status = models.CharField(
        'Status', blank=False, null=False, max_length=50, choices=INTERVIEW_STATUS, db_index=True
    )
    type = models.CharField(
        'Type', blank=False, null=False, max_length=50, choices=INTERVIEW_TYPE, db_index=True
    )
    round = models.IntegerField(
        'Round', blank=False, null=False, db_index=True
    )
    support_tutor = models.CharField(
        'Support Tutor', blank=True, null=True, max_length=50, db_index=True
    )
    student_scheduled_at = models.DateTimeField(
        'Student Scheduled at', blank=True, null=True, db_index=True
    )
    student_timezone = models.CharField(
        'Student TimeZone', blank=True, null=True, choices=INTERVIEW_STUDENT_TIMEZONE, max_length=50
    )
    ist_scheduled_at = models.DateTimeField(
        'IST Scheduled at', blank=True, null=True, db_index=True
    )
    note = models.TextField(
        'Note', blank=True, null=True
    )
    recording_url = models.URLField(
        'Recording URL', blank=True, null=True
    )
    created_at = models.DateTimeField(
        'Created at', blank=False, null=False, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated at', blank=False, null=False, auto_now=True
    )
