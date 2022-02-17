# Generated by Django 3.1.4 on 2022-02-09 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=20, null=True)),
                ('category_id', models.IntegerField()),
                ('category_name', models.CharField(max_length=30)),
                ('product_id', models.IntegerField()),
                ('product_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('allocation', models.BooleanField(default=False)),
                ('table_no', models.IntegerField()),
                ('prepared_by', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
            },
        ),
    ]
