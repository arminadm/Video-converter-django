# Generated by Django 3.2.16 on 2022-11-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_org', models.FileField(upload_to='videos/org/')),
                ('video240', models.FileField(blank=True, null=True, upload_to='videos/240/')),
                ('video360', models.FileField(blank=True, null=True, upload_to='videos/360/')),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]