# Generated by Django 3.2.16 on 2023-01-23 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_gpu_sourced_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sourced_from',
            field=models.CharField(blank=True, max_length=255, verbose_name='Image Sourced From'),
        ),
    ]
