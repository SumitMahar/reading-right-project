# Generated by Django 3.2.5 on 2021-07-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_bag', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='grocery',
            options={'verbose_name_plural': 'Groceries'},
        ),
        migrations.AlterField(
            model_name='grocery',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='grocery',
            name='item_status',
            field=models.CharField(choices=[('BOUGHT', 'BOUGHT'), ('PENDING', 'PENDING'), ('NOT-AVAILABLE', 'NOT AVAILABLE')], default='info', max_length=70),
        ),
    ]
