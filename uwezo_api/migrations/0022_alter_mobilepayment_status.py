# Generated by Django 4.2.4 on 2023-09-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uwezo_api', '0021_alter_mobilepayment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilepayment',
            name='status',
            field=models.CharField(choices=[('initiated', 'Initiated'), ('pending', 'Pending'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='initiated', max_length=16),
        ),
    ]
