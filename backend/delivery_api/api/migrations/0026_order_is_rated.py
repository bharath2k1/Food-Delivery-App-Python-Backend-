# Generated by Django 3.1.2 on 2021-01-23 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_rated',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]