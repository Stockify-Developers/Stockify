# Generated by Django 4.0.3 on 2023-04-02 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stockify', '0014_remove_balance_mtm'),
    ]

    operations = [
        migrations.AddField(
            model_name='balance',
            name='mtm',
            field=models.FloatField(default=0),
        ),
    ]
