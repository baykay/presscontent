# Generated by Django 3.0.3 on 2020-02-18 13:51

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200215_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='users_avatar'),
        ),
    ]
