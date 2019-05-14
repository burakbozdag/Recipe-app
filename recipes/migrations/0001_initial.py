# Generated by Django 2.0.7 on 2019-05-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ingredients', models.TextField(default='ingredients...')),
                ('description', models.TextField()),
                ('difficulty', models.TextField()),
            ],
        ),
    ]
