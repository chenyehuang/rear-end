# Generated by Django 4.2 on 2023-05-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('pics', models.JSONField()),
                ('price', models.FloatField()),
                ('value', models.IntegerField()),
                ('notvalue', models.IntegerField()),
                ('referrer_id', models.CharField(max_length=200)),
                ('recommended_time', models.DateTimeField()),
                ('purchase_method', models.CharField(max_length=200)),
                ('recommendation_reason', models.CharField(max_length=200)),
                ('recent_prices', models.JSONField()),
                ('introduce', models.TextField()),
            ],
        ),
    ]
