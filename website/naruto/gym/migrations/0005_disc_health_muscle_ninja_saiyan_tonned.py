# Generated by Django 3.0.5 on 2020-04-16 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='disc',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='health',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='muscle',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ninja',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='saiyan',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='tonned',
            fields=[
                ('sn', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=200)),
                ('height', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('habit', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
