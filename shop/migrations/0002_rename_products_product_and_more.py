# Generated by Django 4.2.7 on 2023-11-04 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='shop_produc_id_f21274_idx',
            old_name='shop_produc_id_ad469a_idx',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='shop_produc_name_a2070e_idx',
            old_name='shop_produc_name_fa7455_idx',
        ),
        migrations.RenameIndex(
            model_name='product',
            new_name='shop_produc_created_ef211c_idx',
            old_name='shop_produc_created_8eae96_idx',
        ),
    ]
