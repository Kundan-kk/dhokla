# Generated by Django 3.1.3 on 2020-11-15 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0002_appointment_doctor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='symtoms',
            new_name='symptoms',
        ),
    ]