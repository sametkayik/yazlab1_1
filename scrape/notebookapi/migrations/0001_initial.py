# Generated by Django 4.1.2 on 2022-10-14 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
            ],
        ),
    ]
