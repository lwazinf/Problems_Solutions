# Generated by Django 3.0.1 on 2019-12-25 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_auto_20191225_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='color',
            field=models.CharField(default='#9999ff', max_length=20),
        ),
    ]