# Generated by Django 3.2.8 on 2021-10-16 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_auto_20211016_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeecompany',
            name='position',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]