# Generated by Django 4.2 on 2023-04-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0003_merge_20220513_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
