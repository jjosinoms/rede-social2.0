# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import perfis.models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='texto',
            field=models.TextField(verbose_name=perfis.models.Perfil),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name=perfis.models.Perfil),
            preserve_default=True,
        ),
    ]
