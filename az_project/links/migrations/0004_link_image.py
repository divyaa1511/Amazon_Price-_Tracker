# Generated by Django 4.0.5 on 2023-10-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_alter_link_current_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.ImageField(default='images/default_image.jpg', upload_to='images/'),
        ),
    ]
