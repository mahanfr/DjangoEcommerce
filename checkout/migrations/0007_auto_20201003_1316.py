# Generated by Django 3.1.1 on 2020-10-03 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20201003_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promocode',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
