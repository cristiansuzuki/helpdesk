# Generated by Django 4.1.2 on 2022-10-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_alter_chamado_descricao_alter_chamado_resolução_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.CharField(default='', max_length=100),
        ),
    ]
