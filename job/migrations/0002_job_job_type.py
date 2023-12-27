# Generated by Django 5.0 on 2023-12-27 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Full Time'), ('PT', 'Part Time')], default='', max_length=20),
            preserve_default=False,
        ),
    ]
