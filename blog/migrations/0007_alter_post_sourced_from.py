# Generated by Django 3.2.16 on 2023-01-23 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_sourced_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sourced_from',
            field=models.URLField(blank=True, max_length=255, verbose_name='Image Sourced From'),
        ),
    ]
