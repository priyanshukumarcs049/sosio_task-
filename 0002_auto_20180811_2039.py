# Generated by Django 2.1 on 2018-08-11 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPLITWISE', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PERSONS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_person', models.IntegerField()),
                ('who_are_you_with', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='PEOPLE',
        ),
    ]
