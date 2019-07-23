# Generated by Django 2.2.1 on 2019-05-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=32)),
                ('subject_id', models.IntegerField()),
                ('score', models.FloatField()),
                ('student', models.CharField(max_length=32)),
                ('student_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('date', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=32)),
                ('major', models.CharField(max_length=32)),
                ('grade', models.CharField(max_length=32)),
                ('subject', models.ManyToManyField(to='Admin.Subject')),
            ],
        ),
    ]
