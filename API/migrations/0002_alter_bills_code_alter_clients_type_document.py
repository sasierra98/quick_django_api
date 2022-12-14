# Generated by Django 4.1.3 on 2022-11-15 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='code',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Verification code'),
        ),
        migrations.AlterField(
            model_name='clients',
            name='type_document',
            field=models.CharField(choices=[('CC', 'ID Card'), ('TI', 'Card Identification'), ('NIT', 'NIT')], max_length=3, verbose_name='Type document'),
        ),
    ]
