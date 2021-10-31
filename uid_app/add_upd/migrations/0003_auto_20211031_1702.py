# Generated by Django 3.2.8 on 2021-10-31 17:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('add_upd', '0002_alter_request_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='req_address',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('3dd7e622-1ba5-4807-9a95-499aa4c1fa80'), editable=False, primary_key=True, serialize=False)),
                ('From', models.CharField(max_length=10)),
                ('To', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='req_info',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('a7d8a439-ea9d-4611-b8a1-8e83e3fe1c6e'), editable=False, primary_key=True, serialize=False)),
                ('From', models.CharField(max_length=10)),
                ('To', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
