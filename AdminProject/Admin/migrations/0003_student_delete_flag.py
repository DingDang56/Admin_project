# Generated by Django 2.2.1 on 2019-05-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_score_student_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='delete_flag',
            field=models.CharField(default='false', max_length=32),
        ),
    ]
