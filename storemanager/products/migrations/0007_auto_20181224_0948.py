# Generated by Django 2.1.4 on 2018-12-24 09:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181224_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default=uuid.uuid4, max_length=100),
        ),
    ]
