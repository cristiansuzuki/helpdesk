# Generated by Django 4.1.2 on 2022-12-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0008_chamado_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cnpj',
            field=models.CharField(max_length=15),
        ),
    ]
