# Generated by Django 2.1 on 2018-08-12 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SPLITWISE', '0003_auto_20180811_2041'),
    ]

    operations = [
        migrations.CreateModel(
            name='CALCULATION',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount_paid_by_one_person', models.IntegerField()),
                ('Number_of_People_in_group', models.IntegerField()),
            ],
        ),
    ]
