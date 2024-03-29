# Generated by Django 4.0.2 on 2022-02-22 21:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_item_imovel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='name',
            new_name='contato_dono',
        ),
        migrations.RemoveField(
            model_name='imovel',
            name='created',
        ),
        migrations.AddField(
            model_name='imovel',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imovel',
            name='endereco',
            field=models.CharField(default=int, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imovel',
            name='nome_dono',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
