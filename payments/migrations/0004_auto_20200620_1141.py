# Generated by Django 3.0.7 on 2020-06-20 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_payment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='comment',
            field=models.TextField(),
        ),
    ]
