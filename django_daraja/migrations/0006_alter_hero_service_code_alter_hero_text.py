# Generated by Django 4.1.3 on 2023-01-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_daraja', '0005_alter_hero_service_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hero',
            name='service_code',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='hero',
            name='text',
            field=models.CharField(max_length=4),
        ),
    ]
