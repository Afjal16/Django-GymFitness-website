# Generated by Django 4.2.6 on 2023-11-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0014_alter_attendance_selectworkout_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
                ('subtitle', models.TextField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('para', models.TextField()),
            ],
        ),
    ]
