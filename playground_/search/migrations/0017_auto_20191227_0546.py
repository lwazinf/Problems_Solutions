# Generated by Django 3.0.1 on 2019-12-27 05:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('search', '0016_report_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='reporter',
        ),
        migrations.AddField(
            model_name='report',
            name='reporter',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
