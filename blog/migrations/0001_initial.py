# Generated by Django 3.2.13 on 2022-06-19 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.TextField()),
                ('Created_date', models.DateTimeField(auto_now_add=True)),
                ('Published_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]