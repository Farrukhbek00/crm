# Generated by Django 3.1 on 2020-08-13 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]