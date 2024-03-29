# Generated by Django 4.0.5 on 2022-06-21 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='gst_percent',
            new_name='percent_gst',
        ),
        migrations.RenameField(
            model_name='branch',
            old_name='pst_percent',
            new_name='percent_pst',
        ),
        migrations.RemoveField(
            model_name='user',
            name='calculate_gst',
        ),
        migrations.RemoveField(
            model_name='user',
            name='calculate_pst',
        ),
        migrations.AddField(
            model_name='user',
            name='auto_gst',
            field=models.BooleanField(default=True, verbose_name='Auto GST'),
        ),
        migrations.AddField(
            model_name='user',
            name='auto_pst',
            field=models.BooleanField(default=False, verbose_name='Auto PST'),
        ),
    ]
