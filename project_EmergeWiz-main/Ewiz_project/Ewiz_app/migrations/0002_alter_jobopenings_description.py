# Generated by Django 4.2.15 on 2024-08-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ewiz_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopenings',
            name='description',
            field=models.TextField(),
        ),
    ]