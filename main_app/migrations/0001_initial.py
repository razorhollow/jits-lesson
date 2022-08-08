# Generated by Django 4.1 on 2022-08-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('counter', models.IntegerField(default=0)),
                ('video', models.URLField(blank=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
