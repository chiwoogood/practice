# Generated by Django 3.2.13 on 2023-07-03 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0002_auto_20230630_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
