# Generated by Django 4.2.15 on 2024-12-11 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ewiz_app', '0006_jobopenings_job_openings'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobopenings',
            name='logo',
            field=models.ImageField(blank=True, default='images/logo-1.png', null=True, upload_to='images/'),
        ),
    ]
