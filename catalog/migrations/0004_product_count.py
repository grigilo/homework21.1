# Generated by Django 5.0.4 on 2024-05-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
