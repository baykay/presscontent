# Generated by Django 3.0.3 on 2020-02-29 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_avatar_large'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar_large',
        ),
    ]
