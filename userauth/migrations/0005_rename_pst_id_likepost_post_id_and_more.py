# Generated by Django 5.0.2 on 2024-02-24 05:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0004_alter_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likepost',
            old_name='pst_id',
            new_name='post_id',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='captions',
            new_name='caption',
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images'),
        ),
    ]
