# Generated by Django 4.2.1 on 2023-05-26 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Date')),
                ('last_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Last Update')),
                ('name', models.CharField(max_length=15, verbose_name='Name')),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='Native')),
                ('symbol', models.CharField(max_length=15, unique=True, verbose_name='Symbol Code')),
                ('emoji', models.CharField(max_length=1, verbose_name='Emoji')),
                ('rtl', models.BooleanField(default=False, verbose_name='Right To Left')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
    ]
