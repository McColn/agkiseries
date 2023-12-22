# Generated by Django 4.2.6 on 2023-12-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntroVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.FileField(upload_to='videos/')),
            ],
        ),
    ]