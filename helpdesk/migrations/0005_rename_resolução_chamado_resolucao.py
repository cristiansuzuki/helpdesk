# Generated by Django 4.1.2 on 2022-10-27 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0004_rename_tipo_chamado_tipo_chamado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chamado',
            old_name='resolução',
            new_name='resolucao',
        ),
    ]
