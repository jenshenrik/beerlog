# Generated by Django 3.0.6 on 2020-05-19 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('style', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brew_date', models.DateTimeField(verbose_name='date brewed')),
                ('bottle_date', models.DateTimeField(verbose_name='date bottled')),
                ('og', models.IntegerField(default=1000)),
                ('fg', models.IntegerField(default=1000)),
                ('ibu', models.IntegerField(default=0)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.Beer')),
            ],
        ),
    ]
