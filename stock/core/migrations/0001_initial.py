# Generated by Django 4.1.2 on 2022-11-02 03:48

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField()),
                ('account_name', models.CharField(max_length=255)),
                ('bank_name', models.CharField(max_length=255)),
                ('principal', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Holding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISIN', models.CharField(max_length=1024, unique=True)),
                ('holding_name', models.CharField(max_length=255)),
                ('holding_type', models.CharField(max_length=255)),
                ('holding_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Invest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holding_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account')),
                ('holding', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.holding')),
            ],
        ),
    ]
