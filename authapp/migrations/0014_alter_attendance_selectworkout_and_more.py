# Generated by Django 4.2.6 on 2023-11-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_alter_enrollment_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='SelectWorkout',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='TrainedBy',
            field=models.CharField(max_length=200, null=True),
        ),
    ]