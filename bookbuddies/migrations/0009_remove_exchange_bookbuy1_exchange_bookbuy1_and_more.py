# Generated by Django 4.0.3 on 2022-04-24 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookbuddies', '0008_exchange_bookbuy2_exchange_bookbuy3_exchange_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exchange',
            name='bookBuy1',
        ),
        migrations.AddField(
            model_name='exchange',
            name='bookBuy1',
            field=models.ManyToManyField(blank=True, related_name='bookBuy1', to='bookbuddies.book'),
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='bookBuy2',
        ),
        migrations.AddField(
            model_name='exchange',
            name='bookBuy2',
            field=models.ManyToManyField(blank=True, related_name='bookBuy2', to='bookbuddies.book'),
        ),
        migrations.RemoveField(
            model_name='exchange',
            name='bookBuy3',
        ),
        migrations.AddField(
            model_name='exchange',
            name='bookBuy3',
            field=models.ManyToManyField(blank=True, related_name='bookBuy3', to='bookbuddies.book'),
        ),
    ]
