# Generated by Django 5.0.6 on 2025-01-13 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0006_alter_leads_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=30)),
                (
                    'organisation',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='Leads.userprofile',
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name='leads',
            name='category',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='Leads.category',
            ),
        ),
    ]
