# Generated by Django 4.2 on 2025-02-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='new_field',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
