# Generated by Django 3.2.8 on 2021-10-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20211016_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='companycollaboration',
            name='collaboration_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]