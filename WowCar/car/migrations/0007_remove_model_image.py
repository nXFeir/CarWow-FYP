# Generated by Django 4.0.4 on 2022-11-02 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_alter_variant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='image',
        ),
    ]
