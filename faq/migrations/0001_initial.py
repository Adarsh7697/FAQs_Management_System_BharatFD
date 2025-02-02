# Generated by Django 4.2 on 2025-02-01 18:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', ckeditor.fields.RichTextField()),
                ('question_hi', models.TextField(blank=True, null=True)),
                ('question_bn', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
