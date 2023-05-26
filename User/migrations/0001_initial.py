# Generated by Django 4.2.1 on 2023-05-26 22:17

import Utils.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Address', '0001_initial'),
        ('Restaurant', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(blank=True, max_length=17, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='mobile')),
                ('otp', models.CharField(blank=True, max_length=25, null=True, verbose_name='OTP')),
                ('email', models.EmailField(error_messages={'unique': 'E-Mail Is User'}, max_length=200, unique=True, verbose_name='E-Mail')),
                ('username', models.CharField(error_messages={'unique': 'User Name Is User. choose Another'}, max_length=30, unique=True, verbose_name='User Name')),
                ('is_active', models.BooleanField(default=False, verbose_name='is Active')),
                ('is_verified', models.BooleanField(default=False, verbose_name='is Verfied')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is Super User')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('image', models.ImageField(blank=True, default="images/{instance.__class__.__name__}/default.jpg' %}", null=True, upload_to=Utils.models.upload_to, verbose_name='Image')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='First Name')),
                ('family_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Family Name')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth Date')),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True, verbose_name='Gender')),
                ('facebook_link', models.URLField(blank=True, null=True, verbose_name='FaceBook Link')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profiles', to='Address.address', verbose_name='Address')),
                ('language', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Language.language', verbose_name='Language')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='UserRestaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='is Favorite')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('review', models.FloatField(verbose_name='Review')),
                ('likes', models.SmallIntegerField(default=0, verbose_name='Likes')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Choiced_Users', to='Restaurant.restaurant', verbose_name='Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Restaurants', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'User Restaurant',
                'verbose_name_plural': 'Users Restaurants',
                'unique_together': {('user', 'restaurant')},
            },
        ),
    ]
