# Generated by Django 5.0.6 on 2024-06-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('description', models.TextField()),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
