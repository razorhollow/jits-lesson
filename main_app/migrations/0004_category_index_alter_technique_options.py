# Generated by Django 4.1 on 2022-08-09 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_technique_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='technique',
            options={'ordering': ['category', '-modified']},
        ),
    ]
