# Generated by Django 3.1.4 on 2022-02-11 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_auto_20220209_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default='media', upload_to=''),
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chef',
            name='chef_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chef',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='chef',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order_id',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='prepared_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
