# Generated by Django 3.2.16 on 2023-01-22 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20230122_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='gpu',
            name='sourced_from',
            field=models.CharField(blank=True, max_length=255, verbose_name='Content Sourced From'),
        ),
    ]
