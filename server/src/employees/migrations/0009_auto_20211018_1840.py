# Generated by Django 3.2.8 on 2021-10-18 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0006_alter_companycollaboration_companies'),
        ('employees', '0008_employeelanguage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='languages',
        ),
        migrations.AlterField(
            model_name='employeecompany',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company'),
        ),
    ]
