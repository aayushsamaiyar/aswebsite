# Generated by Django 3.2.1 on 2021-07-23 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, verbose_name='')),
                ('email', models.CharField(max_length=40, verbose_name='')),
                ('phone', models.CharField(max_length=15, verbose_name='')),
                ('content', models.CharField(max_length=2000, verbose_name='')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
