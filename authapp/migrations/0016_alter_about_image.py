# Generated by Django 4.2.6 on 2023-11-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about'),
        ),
    ]