# Generated by Django 3.0.3 on 2020-03-20 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sevapp', '0006_election'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='id',
        ),
        migrations.AlterField(
            model_name='election',
            name='election_name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
