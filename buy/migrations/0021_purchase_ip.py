# Generated by Django 2.1.2 on 2018-10-15 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0020_purchase_nonce'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
