# Generated by Django 3.1.7 on 2021-02-24 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_ingredients_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='Customers',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.customers'),
            preserve_default=False,
        ),
    ]
