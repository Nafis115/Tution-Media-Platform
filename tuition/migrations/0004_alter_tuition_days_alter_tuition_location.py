# Generated by Django 5.0.6 on 2024-09-12 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuition', '0003_dayschoice_remove_tuition_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='days',
            field=models.ManyToManyField(blank=True, to='tuition.dayschoice'),
        ),
        migrations.AlterField(
            model_name='tuition',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
