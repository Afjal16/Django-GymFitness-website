# Generated by Django 4.2.6 on 2023-11-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phonenumber',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='DOB',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='FullName',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Gender',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='PhoneNumber',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='Reference',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='SelectMembershipplan',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='SelectTrainer',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='phone',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.IntegerField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]