# Generated by Django 4.2.8 on 2024-01-10 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_collection_featured_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orderitems', to='store.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store.collection'),
        ),
    ]
