# Generated by Django 2.2.6 on 2019-12-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemoapp', '0004_auto_20191123_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='button_id',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='like',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]