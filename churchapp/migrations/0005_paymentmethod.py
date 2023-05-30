# Generated by Django 3.2.16 on 2023-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchapp', '0004_event_impact_impactcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('method', models.CharField(max_length=100)),
                ('paybill', models.IntegerField(blank=True, null=True)),
                ('till', models.IntegerField(blank=True, null=True)),
                ('account', models.CharField(max_length=255)),
            ],
        ),
    ]
