# Generated by Django 2.1.15 on 2020-03-21 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proj_info',
            options={'permissions': (('upload_code', '可以上传代码'),)},
        ),
    ]