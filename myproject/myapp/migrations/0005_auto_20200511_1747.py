# Generated by Django 2.1.3 on 2020-05-11 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20200511_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='req',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
