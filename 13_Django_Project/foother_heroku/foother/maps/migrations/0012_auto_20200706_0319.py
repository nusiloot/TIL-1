# Generated by Django 2.1.15 on 2020-07-05 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20200705_1859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
    ]
