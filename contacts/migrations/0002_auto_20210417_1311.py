# Generated by Django 2.0.7 on 2021-04-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='contact_dete',
            new_name='contact_date',
        ),
    ]
