# Generated by Django 2.1.15 on 2020-06-26 01:51

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200625_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
    ]
