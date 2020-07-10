# Generated by Django 3.0.5 on 2020-07-05 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foods', '0004_auto_20200704_1245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foods.Product')),
            ],
        ),
    ]
