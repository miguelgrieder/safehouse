# Generated by Django 4.0.2 on 2022-02-23 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_sensor_imovel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacao',
            name='imovel_id',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]