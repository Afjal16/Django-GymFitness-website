# Generated by Django 4.2.6 on 2023-11-20 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0016_alter_about_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='gallery')),
                ('pera', models.TextField(max_length=200)),
                ('rate', models.CharField(max_length=7)),
            ],
        ),
    ]