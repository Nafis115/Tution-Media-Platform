# Generated by Django 5.0.6 on 2024-09-12 10:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin_panel', '0001_initial'),
        ('tutor', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('General_Math', 'General Math'), ('Bangla', 'Bangla'), ('English', 'English'), ('General_Science', 'General Science'), ('Religion', 'Religion'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Biology', 'Biology'), ('Higher_Math', 'Higher Math'), ('All_Subjects', 'All Subjects')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tuition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Tuition For', help_text='Title of the tuition', max_length=100)),
                ('tuition_class', models.CharField(choices=[('Class 1', 'Class 1'), ('Class 2', 'Class 2'), ('Class 3', 'Class 3'), ('Class 4', 'Class 4'), ('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('Class 7', 'Class 7'), ('Class 8', 'Class 8'), ('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('HSC 1', 'HSC-1st_Year'), ('HSC 2', 'HSC-2nd_Year')], help_text='Class for which tuition is offered', max_length=50)),
                ('availability', models.BooleanField(default=True, help_text='Availability status of the tuition')),
                ('description', models.TextField(help_text='Detailed description of the tuition')),
                ('medium', models.CharField(choices=[('Bangla', 'Bangla_Medium'), ('English', 'English_Version')], help_text='Medium of instruction', max_length=50)),
                ('student_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], help_text='Gender of students', max_length=50)),
                ('preferred_tutor_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], help_text='Preferred gender of tutor', max_length=50)),
                ('tutoring_time', models.CharField(choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], help_text='Time for tutoring', max_length=20)),
                ('number_of_students', models.PositiveIntegerField(default=1, help_text='Number of students')),
                ('salary', models.DecimalField(decimal_places=2, help_text='Salary offered per month', max_digits=10)),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_panel.adminmodel')),
                ('subjects', models.ManyToManyField(help_text='Subjects taught in this tuition', related_name='tuitions', to='tuition.subjectchoice')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=5)),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.tutormodel')),
                ('tuition', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tuition.tuition')),
            ],
        ),
    ]
