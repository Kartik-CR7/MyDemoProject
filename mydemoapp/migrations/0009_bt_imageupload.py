# Generated by Django 2.2.6 on 2019-12-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydemoapp', '0008_auto_20191212_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='BT_Imageupload',
            fields=[
                ('Image_id', models.AutoField(primary_key=True, serialize=False)),
                ('Image_name', models.CharField(default='Unnamed_Image', max_length=200)),
                ('Image', models.ImageField(blank=True, upload_to='profile_image/')),
            ],
        ),
    ]