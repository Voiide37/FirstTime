# Generated by Django 5.1.3 on 2024-11-18 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task', models.CharField(max_length=300)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
