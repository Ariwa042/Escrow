# Generated by Django 4.2.12 on 2024-09-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_is_active_alter_user_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='account_balance',
            field=models.DecimalField(decimal_places=8, default=0, max_digits=20),
        ),
    ]
