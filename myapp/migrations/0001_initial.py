# Generated by Django 4.1.5 on 2023-02-03 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60)),
                ('phone', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=130)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
