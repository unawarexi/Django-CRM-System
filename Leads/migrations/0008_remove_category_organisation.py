# Generated by Django 5.0.6 on 2025-01-13 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0007_category_leads_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='organisation',
        ),
    ]
