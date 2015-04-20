# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0004_delete_shortedurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldb',
            name='urlCut',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
