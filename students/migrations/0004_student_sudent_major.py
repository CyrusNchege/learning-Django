# Generated by Django 4.1.5 on 2023-02-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_student_student_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sudent_major',
            field=models.CharField(default='undeclared', max_length=100),
        ),
    ]
