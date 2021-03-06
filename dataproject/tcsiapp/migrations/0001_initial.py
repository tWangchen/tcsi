# Generated by Django 3.2.3 on 2021-05-30 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TcsiElement',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('element_no', models.CharField(blank=True, max_length=255, null=True)),
                ('page_title', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=5000, null=True)),
                ('code_category', models.CharField(blank=True, max_length=255, null=True)),
                ('element_type', models.CharField(blank=True, max_length=255, null=True)),
                ('width', models.CharField(blank=True, max_length=255, null=True)),
                ('version_revision_date', models.CharField(blank=True, max_length=255, null=True)),
                ('version', models.CharField(blank=True, max_length=255, null=True)),
                ('years_version_active', models.CharField(blank=True, max_length=255, null=True)),
                ('sub_header', models.CharField(blank=True, max_length=255, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('meaning', models.CharField(blank=True, max_length=5000, null=True)),
                ('derivation', models.CharField(blank=True, max_length=255, null=True)),
                ('spec_flag', models.CharField(blank=True, max_length=255, null=True)),
                ('retired', models.CharField(blank=True, max_length=255, null=True)),
                ('page_access_timestamp', models.DateField()),
                ('page_url', models.CharField(blank=True, max_length=255, null=True)),
                ('page_harvestor', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tcsi_element',
                'managed': False,
            },
        ),
    ]
