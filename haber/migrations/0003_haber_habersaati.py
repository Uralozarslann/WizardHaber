# Generated by Django 4.2.4 on 2023-10-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haber', '0002_haber_habersehir'),
    ]

    operations = [
        migrations.AddField(
            model_name='haber',
            name='haberSaati',
            field=models.TimeField(blank=True, null=True, verbose_name='haber saat'),
        ),
    ]
