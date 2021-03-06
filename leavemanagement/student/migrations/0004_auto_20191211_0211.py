# Generated by Django 3.0 on 2019-12-10 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
        ('student', '0003_application_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='faculty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='faculty.Faculty'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='is_pending',
            field=models.BooleanField(default=True),
        ),
    ]
