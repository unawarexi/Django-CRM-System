# Generated by Django 5.0.6 on 2025-01-13 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0005_leads_organisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='organisation',
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='Leads.userprofile',
            ),
        ),
    ]
