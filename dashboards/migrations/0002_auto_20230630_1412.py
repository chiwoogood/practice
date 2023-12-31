# Generated by Django 3.2.13 on 2023-06-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='title',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='dashboard',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
