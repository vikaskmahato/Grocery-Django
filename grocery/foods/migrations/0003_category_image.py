# Generated by Django 3.0.5 on 2020-07-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_auto_20200704_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/category/'),
        ),
    ]
