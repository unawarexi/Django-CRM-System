# Generated by Django 5.0.6 on 2025-01-13 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0003_user_is_agent_user_is_organisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leads',
            name='agent',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='Leads.agent',
            ),
        ),
    ]
