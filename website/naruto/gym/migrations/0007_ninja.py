# Generated by Django 3.0.5 on 2020-04-16 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0006_auto_20200415_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ninja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emails', models.CharField(max_length=50)),
                ('phones', models.CharField(max_length=50)),
                ('ages', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('habit', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=800)),
            ],
        ),
    ]
