# Generated by Django 3.1.7 on 2021-07-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210714_2215'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
