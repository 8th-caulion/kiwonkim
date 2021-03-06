# Generated by Django 2.1.3 on 2020-05-11 17:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='req',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='req',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
