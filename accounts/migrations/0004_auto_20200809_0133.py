# Generated by Django 3.1 on 2020-08-08 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customer_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
