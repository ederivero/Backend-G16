# Generated by Django 5.0.2 on 2024-02-24 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_creacion_tablas_ingredientes_preparaciones'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='plato',
            new_name='platoId'
        ),
        migrations.RenameField(
            model_name='preparacion',
            old_name='plato',
            new_name='platoId'
        ),
        migrations.AlterUniqueTogether(
            name='preparacion',
            unique_together={('orden', 'platoId')},
        ),
        migrations.AddField(
            model_name='plato',
            name='tipo',
            field=models.TextField(choices=[('entrada', 'ENTRADA'), (
                'plato_de_fondo', 'PLATO DE FONDO'), ('postre', 'POSTRE')], default='entrada'),
        ),
    ]
