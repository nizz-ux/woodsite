# Generated by Django 4.2.15 on 2024-09-12 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_complain_details_c_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='old_furniture',
            name='old_furniture_image',
            field=models.ImageField(null=True, upload_to='photo'),
        ),
    ]