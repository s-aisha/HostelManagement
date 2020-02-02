# Generated by Django 2.1 on 2019-10-30 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('place', models.CharField(max_length=75)),
                ('reason', models.CharField(max_length=75)),
                ('exit_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateTimeField(null=True)),
                ('out_time', models.DateTimeField(auto_now_add=True)),
                ('degree', models.CharField(max_length=75)),
                ('branch', models.CharField(max_length=75)),
                ('year', models.IntegerField()),
                ('block_name', models.CharField(max_length=75)),
                ('room_no', models.IntegerField()),
                ('rt_name', models.CharField(max_length=75)),
                ('check_with', models.CharField(max_length=75)),
                ('pass_available', models.CharField(max_length=75)),
            ],
        ),
    ]
