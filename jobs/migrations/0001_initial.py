# Generated by Django 5.1 on 2024-08-10 11:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('email', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('company_logo', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('user_type', models.CharField(max_length=30)),
                ('company_name', models.CharField(max_length=100)),
                ('company_ceo', models.CharField(max_length=100)),
                ('company_established', models.DateField()),
                ('company_location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post_jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('jobtype', models.CharField(max_length=50, null=True)),
                ('salary', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(max_length=400)),
                ('experience', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20, null=True)),
                ('skills', models.CharField(max_length=200)),
                ('creation_date', models.DateField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.company')),
            ],
        ),
        migrations.CreateModel(
            name='job_seeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('phone_number', models.IntegerField()),
                ('profile_image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('occupation', models.CharField(max_length=100, null=True)),
                ('age', models.CharField(max_length=15, null=True)),
                ('user_type', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=100, null=True)),
                ('resume', models.FileField(null=True, upload_to='')),
                ('skills', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=15, null=True)),
                ('years_experience', models.CharField(max_length=15, null=True)),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('company_address', models.CharField(max_length=50, null=True)),
                ('position', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookmarks', models.ManyToManyField(blank=True, to='jobs.post_jobs')),
            ],
        ),
        migrations.CreateModel(
            name='apply_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=200)),
                ('email', models.CharField(max_length=100, null=True)),
                ('jobtype', models.CharField(max_length=50, null=True)),
                ('resume', models.FileField(upload_to='')),
                ('apply_date', models.DateField()),
                ('status', models.CharField(max_length=50, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job_seeker')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.post_jobs')),
            ],
        ),
    ]