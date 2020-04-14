# Generated by Django 3.0.3 on 2020-02-29 23:39

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_large',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='users_avatar'),
        ),
    ]
