# Generated by Django 5.0.6 on 2024-08-16 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tution', '0015_review_tuition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=5),
        ),
    ]