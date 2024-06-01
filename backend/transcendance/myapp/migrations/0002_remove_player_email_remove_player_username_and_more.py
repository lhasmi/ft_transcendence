# Generated by Django 5.0.3 on 2024-04-26 19:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
        migrations.RemoveField(
            model_name='player',
            name='username',
        ),
        migrations.AddField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]