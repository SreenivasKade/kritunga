# Generated by Django 3.1.4 on 2022-02-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('chef_name', models.CharField(max_length=30)),
                ('chef_image', models.ImageField(default='media', upload_to='')),
                ('orders_completed', models.IntegerField(default=0)),
                ('description', models.TextField(blank=True, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category_name', models.ManyToManyField(to='testapp.Category')),
            ],
            options={
                'verbose_name': 'Chef',
                'verbose_name_plural': 'Chefs',
            },
        ),
    ]