# Generated by Django 4.2.6 on 2023-12-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='media/')),
            ],
        ),
    ]
