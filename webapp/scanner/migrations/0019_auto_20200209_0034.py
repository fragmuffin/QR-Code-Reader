# Generated by Django 2.1.7 on 2020-02-08 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0018_event_loc_block'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='supplemental_address_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='supplemental_address_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='supplemental_address_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
