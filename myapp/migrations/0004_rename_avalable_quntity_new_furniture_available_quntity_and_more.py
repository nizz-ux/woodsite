# Generated by Django 4.2.15 on 2024-08-31 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_brand_table_new_furniture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='new_furniture',
            old_name='avalable_quntity',
            new_name='available_quntity',
        ),
        migrations.CreateModel(
            name='rent_furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_furniture_name', models.CharField(max_length=30)),
                ('rent_furniture_description', models.TextField()),
                ('available_quntity', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=30)),
                ('rent_brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand_table')),
                ('rent_furniture_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.furniture_category')),
            ],
        ),
        migrations.CreateModel(
            name='old_furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_furniture_description', models.TextField()),
                ('old_furniture_price', models.IntegerField()),
                ('old_furniture_qunitiy', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')], max_length=30)),
                ('old_furniture_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.brand_table')),
                ('old_furniture_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.furniture_category')),
            ],
        ),
    ]
