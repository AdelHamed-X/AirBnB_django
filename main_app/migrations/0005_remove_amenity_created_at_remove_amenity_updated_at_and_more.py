# Generated by Django 5.0.3 on 2024-04-03 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_amenity_id_alter_city_id_alter_place_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='amenity',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='city',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='city',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='place',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='place',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='state',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='state',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_at',
        ),
    ]
