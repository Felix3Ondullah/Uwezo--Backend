# Generated by Django 4.2.4 on 2023-08-22 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uwezo_api', '0004_insurer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msisdn', models.PositiveIntegerField()),
                ('imei', models.BigIntegerField(default=0)),
                ('car_id', models.PositiveIntegerField(default=0)),
                ('platform', models.CharField(choices=[('protrack', 'ProTrackGPS'), ('whatsgps', 'WhatsGPS')], default='protrack', max_length=16)),
                ('autoswitch', models.BooleanField(default=True)),
                ('expiry_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('on', 'On'), ('off', 'Off'), ('inactive', 'Inactive')], default='inactive', max_length=16)),
                ('command', models.CharField(blank=True, max_length=8)),
                ('command_response', models.BooleanField(default=False)),
                ('document', models.TextField(blank=True)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uwezo_api.vehicle')),
            ],
        ),
    ]
