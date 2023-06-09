# Generated by Django 3.2.16 on 2023-04-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IaqData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ids', models.FloatField(null=True)),
                ('macAddress', models.CharField(max_length=120, null=True)),
                ('iaqScore', models.FloatField(null=True)),
                ('pm10', models.FloatField(null=True)),
                ('pm25', models.FloatField(null=True)),
                ('pm1', models.FloatField(null=True)),
                ('co2', models.FloatField(null=True)),
                ('voc', models.FloatField(null=True)),
                ('temp', models.FloatField(null=True)),
                ('humd', models.FloatField(null=True)),
                ('outAvgTemp', models.FloatField(null=True)),
                ('rainfall', models.CharField(max_length=2, null=True)),
                ('time', models.CharField(max_length=120, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
