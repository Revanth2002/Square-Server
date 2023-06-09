# Generated by Django 4.2.1 on 2023-05-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(blank=True, max_length=512, null=True)),
                ('industry', models.CharField(blank=True, max_length=512, null=True)),
                ('group', models.CharField(blank=True, max_length=512, null=True)),
                ('api_endpoints', models.CharField(blank=True, max_length=512, null=True)),
                ('group_enabled', models.BooleanField(default=True)),
                ('template_type', models.CharField(blank=True, max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.CharField(blank=True, max_length=256, null=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('expirable', models.BooleanField(default=False)),
                ('amount', models.CharField(blank=True, max_length=256, null=True)),
                ('details', models.JSONField(blank=True, default=list, null=True)),
                ('plan_enabed', models.BooleanField(default=True)),
                ('subscription', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.subscriptionmodel')),
            ],
        ),
    ]
