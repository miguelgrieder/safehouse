# Generated by Django 4.0.2 on 2022-02-23 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_switch_bool_status_status_bool'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='imovel_id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
