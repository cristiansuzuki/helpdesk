# Generated by Django 4.1.2 on 2022-12-14 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0012_alter_chamado_tipo_chamado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='tipo_chamado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.tipochamado'),
        ),
    ]
