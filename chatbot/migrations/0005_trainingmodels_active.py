# Generated by Django 3.2.8 on 2021-10-28 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_trainingmodels_insert_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainingmodels',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]