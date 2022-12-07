# Generated by Django 3.0.5 on 2020-04-14 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=20)),
                ('contents', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
