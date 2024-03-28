# Generated by Django 5.0.3 on 2024-03-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('profile_picture', models.URLField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('travel_interests', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]