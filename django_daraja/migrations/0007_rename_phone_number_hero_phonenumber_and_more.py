# Generated by Django 4.1.3 on 2023-01-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_daraja', '0006_alter_hero_service_code_alter_hero_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hero',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='service_code',
            new_name='servicecode',
        ),
        migrations.RenameField(
            model_name='hero',
            old_name='session_id',
            new_name='sessionid',
        ),
    ]