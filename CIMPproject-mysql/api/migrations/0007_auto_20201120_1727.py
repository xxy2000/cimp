# Generated by Django 3.1.2 on 2020-11-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201120_1721'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='students',
            unique_together=set(),
        ),
        migrations.AlterIndexTogether(
            name='students',
            index_together=set(),
        ),
    ]
