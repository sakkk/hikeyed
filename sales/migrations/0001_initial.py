# Generated by Django 3.0 on 2019-12-11 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_date', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to='customer.Customer')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales.Payment')),
            ],
        ),
        migrations.CreateModel(
            name='SalesDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('sub_total', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product', to='product.Product')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sales')),
            ],
        ),
    ]
