# Generated by Django 4.2.7 on 2023-11-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_photo_alter_userprofile_user_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default='No title', max_length=50),
        ),
    ]
