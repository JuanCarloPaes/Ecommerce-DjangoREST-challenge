# Generated by Django 4.2.5 on 2023-09-24 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_review_product'),
        ('order', '0003_orderitems_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderItems',
            new_name='OrderItem',
        ),
    ]
