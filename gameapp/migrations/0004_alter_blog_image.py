# Generated by Django 3.2.6 on 2021-08-15 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapp', '0003_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]