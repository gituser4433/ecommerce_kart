# Generated by Django 3.1.7 on 2021-07-14 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_account_is_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='phone_numner',
            new_name='phone_number',
        ),
    ]
