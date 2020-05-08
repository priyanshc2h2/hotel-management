# Generated by Django 3.0.5 on 2020-04-29 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('adharID', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('mobileno', models.IntegerField()),
                ('members', models.IntegerField()),
                ('cid', models.DateField()),
                ('cot', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='room_no',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='room_price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
