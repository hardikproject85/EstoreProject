# Generated by Django 3.0 on 2021-04-21 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user_usertype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('kids', 'kids'), ('mens', 'mens'), ('womens', 'womens')], max_length=100)),
                ('product_brand', models.CharField(max_length=100)),
                ('product_color', models.CharField(max_length=100)),
                ('product_size', models.IntegerField()),
                ('product_price', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='ProductImages/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.User')),
            ],
        ),
    ]
