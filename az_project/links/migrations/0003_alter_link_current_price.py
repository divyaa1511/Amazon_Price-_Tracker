# Generated by Django 4.0.5 on 2023-10-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_alter_link_current_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='current_price',
            field=models.FloatField(blank=True),
        ),
    ]
