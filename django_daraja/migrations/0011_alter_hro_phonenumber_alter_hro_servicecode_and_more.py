# Generated by Django 4.1.3 on 2023-01-10 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_daraja', '0010_delete_hero_alter_hro_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hro',
            name='phoneNumber',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='hro',
            name='serviceCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hro',
            name='text',
            field=models.CharField(max_length=4),
        ),
    ]
