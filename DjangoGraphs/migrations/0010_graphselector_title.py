# Generated by Django 2.2.3 on 2019-07-05 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoGraphs', '0009_auto_20190704_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphselector',
            name='title',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]
