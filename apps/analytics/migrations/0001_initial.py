# Generated by Django 5.1.6 on 2025-02-16 16:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthMetric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metric_type', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('recorded_at', models.DateTimeField()),
                ('analysis_data', models.JSONField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analytics_health_metrics', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Health Metric',
                'verbose_name_plural': 'Health Metrics',
                'db_table': 'analytics_health_metrics',
                'ordering': ['-recorded_at'],
            },
        ),
        migrations.CreateModel(
            name='UserActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=50)),
                ('activity_data', models.JSONField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('user_agent', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Activity',
                'verbose_name_plural': 'User Activities',
                'db_table': 'analytics_user_activity',
                'ordering': ['-timestamp'],
                'indexes': [models.Index(fields=['user', 'activity_type'], name='analytics_u_user_id_fab10a_idx'), models.Index(fields=['timestamp'], name='analytics_u_timesta_1d8413_idx')],
            },
        ),
    ]
