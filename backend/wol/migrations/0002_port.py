# Generated by Django 4.0.2 on 2022-02-18 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('name', models.SlugField()),
            ],
        ),
    ]