# Generated by Django 4.2.4 on 2023-08-22 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=16)),
                ('middle_name', models.CharField(blank=True, max_length=16, null=True)),
                ('last_name', models.CharField(max_length=16)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('document_type', models.CharField(blank=True, choices=[('national_id', 'National ID'), ('passport', 'Passport'), ('military_id', 'Miliary ID')], default='national_id', max_length=16, null=True)),
                ('document_number', models.CharField(blank=True, max_length=8, null=True)),
                ('msisdn', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('document', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
