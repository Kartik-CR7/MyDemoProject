# Generated by Django 2.2.6 on 2019-12-11 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemoapp', '0006_auto_20191212_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='button_id',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
