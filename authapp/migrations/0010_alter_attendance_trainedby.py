# Generated by Django 4.2.6 on 2023-11-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_alter_attendance_selectworkout_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='TrainedBy',
            field=models.CharField(default='Harry', max_length=200),
        ),
    ]
