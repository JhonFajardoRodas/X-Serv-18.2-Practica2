# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0002_shortedurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='urldb',
            name='urlCut',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
