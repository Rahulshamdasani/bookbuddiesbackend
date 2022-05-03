# Generated by Django 4.0.3 on 2022-04-23 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookbuddies', '0005_alter_book_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookSell', models.ManyToManyField(blank=True, related_name='bookSell', to='bookbuddies.book')),
            ],
        ),
    ]
