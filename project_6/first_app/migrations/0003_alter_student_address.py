# Generated by Django 5.0.6 on 2024-06-21 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_student_father_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(),
        ),
    ]
