# Generated by Django 2.2.7 on 2019-12-16 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_page', '0006_todoitem_timecreated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='Timecreated',
            field=models.DateTimeField(),
        ),
    ]
