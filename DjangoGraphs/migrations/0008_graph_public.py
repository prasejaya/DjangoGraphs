# Generated by Django 2.2.3 on 2019-07-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoGraphs', '0007_auto_20190704_0855'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]