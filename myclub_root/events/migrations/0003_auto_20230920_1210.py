# Generated by Django 3.2.21 on 2023-09-20 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20230911_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email_address',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='Contact Phone'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Web Address'),
        ),
    ]
