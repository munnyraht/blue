# Generated by Django 2.2.2 on 2019-07-16 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=38, null=True)),
                ('Surname', models.CharField(max_length=38, null=True)),
                ('Role', models.CharField(max_length=38, null=True)),
                ('EmailAddress', models.EmailField(max_length=254, null=True)),
                ('MobileNumber', models.DecimalField(decimal_places=0, max_digits=11, null=True)),
                ('Password', models.CharField(max_length=38, null=True)),
                ('active', models.CharField(default='pending', max_length=100)),
                ('ConfirmPassword', models.CharField(max_length=38, null=True)),
                ('Created', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='personalinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MiddleName', models.CharField(max_length=32)),
                ('MobileNumber2', models.IntegerField()),
                ('DateOfBirth', models.DateField()),
                ('MaritalStatus', models.CharField(max_length=50)),
                ('PlaceOfBirth', models.CharField(max_length=100)),
                ('NumberOfDependent', models.IntegerField()),
                ('DateAtAddress', models.DateField()),
                ('HomeAddress', models.TextField()),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.user')),
            ],
        ),
        migrations.CreateModel(
            name='bvn_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bvn', models.IntegerField()),
                ('first_name', models.CharField(max_length=38, null=True)),
                ('last_name', models.CharField(max_length=38, null=True)),
                ('middle_name', models.CharField(max_length=38, null=True)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('registration_date', models.DateField()),
                ('enrollment_bank', models.IntegerField()),
                ('enrollment_branch', models.CharField(max_length=38, null=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.user')),
            ],
        ),
    ]
