# Generated by Django 4.0.6 on 2022-07-30 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_band_like_news'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_news',
        ),
    ]
