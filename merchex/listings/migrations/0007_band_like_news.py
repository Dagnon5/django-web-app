# Generated by Django 4.0.6 on 2022-07-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_alter_listing_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='like_news',
            field=models.BooleanField(default=False),
        ),
    ]
