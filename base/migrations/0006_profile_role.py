# Generated by Django 5.1.2 on 2024-10-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_profile_avatar_profile_bio_profile_birth_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor'), ('approver', 'Approver')], default='student', max_length=20),
        ),
    ]
