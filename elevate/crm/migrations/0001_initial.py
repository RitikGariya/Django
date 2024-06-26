# Generated by Django 5.0.4 on 2024-06-03 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirmDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(max_length=255)),
                ('mobile_no', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('gstn_no', models.CharField(max_length=15)),
                ('msme_status', models.BooleanField(default=False)),
                ('certification_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
