# Generated by Django 2.0.5 on 2019-08-22 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('thumbnail_url', models.CharField(max_length=2048)),
                ('price', models.FloatField()),
                ('stock', models.BooleanField(default=False)),
                ('product_description', models.TextField(blank=True, default=None, null=True)),
                ('upc', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='scraper.Categories'),
        ),
    ]
