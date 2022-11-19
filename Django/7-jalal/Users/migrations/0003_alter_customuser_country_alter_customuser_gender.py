# Generated by Django 4.0.4 on 2022-11-16 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_customuser_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.CharField(default='Iran', editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]