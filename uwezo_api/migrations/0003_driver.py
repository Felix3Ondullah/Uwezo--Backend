# Generated by Django 4.2.4 on 2023-08-22 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uwezo_api', '0002_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('middle_name', models.CharField(blank=True, max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('date_of_birth', models.DateField()),
                ('document_type', models.CharField(choices=[('national_id', 'National ID'), ('passport', 'Passport'), ('military_id', 'Miliary ID')], default='national_id', max_length=16)),
                ('document_number', models.CharField(max_length=8)),
                ('msisdn', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('document', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('suspended', 'Suspended'), ('closed', 'Closed')], default='active', max_length=16)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uwezo_api.partner')),
            ],
        ),
    ]
