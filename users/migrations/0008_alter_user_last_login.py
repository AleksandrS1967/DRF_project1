# Generated by Django 5.0.6 on 2024-07-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_payment_payment_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время последнего посещения'),
        ),
    ]