# Generated by Django 3.2.16 on 2023-05-30 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchapp', '0007_alter_paymentmethod_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='account',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
