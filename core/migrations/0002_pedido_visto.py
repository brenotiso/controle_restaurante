# Generated by Django 2.2.2 on 2019-06-30 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='visto',
            field=models.BooleanField(default=False),
        ),
    ]
