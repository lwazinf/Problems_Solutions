# Generated by Django 3.0.1 on 2019-12-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20191225_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(default='crimson', max_length=20),
        ),
    ]