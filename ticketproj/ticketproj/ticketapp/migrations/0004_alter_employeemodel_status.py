# Generated by Django 3.2.5 on 2021-09-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0003_auto_20210918_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='status',
            field=models.CharField(choices=[('not resolved', 'not resolved'), ('resolved', 'resolved')], default='Not resolved', max_length=50),
        ),
    ]
