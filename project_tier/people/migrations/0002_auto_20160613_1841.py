# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-13 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PersonCategoryRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='people.PersonCategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='personpagetag',
            name='content_object',
        ),
        migrations.RemoveField(
            model_name='personpagetag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='personpage',
            name='job_titles',
        ),
        migrations.AddField(
            model_name='personpage',
            name='academic_job_title',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='personpage',
            name='fellowship_year',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='personpage',
            name='main_job_title',
            field=models.TextField(blank=True),
        ),
        migrations.DeleteModel(
            name='PersonPageTag',
        ),
        migrations.AddField(
            model_name='personcategoryrelationship',
            name='person',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_category_relationship', to='people.PersonPage'),
        ),
    ]
