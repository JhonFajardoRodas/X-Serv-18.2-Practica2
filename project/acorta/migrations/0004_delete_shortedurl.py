# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acorta', '0003_urldb_urlcut'),
    ]

    operations = [
        migrations.DeleteModel(
            name='shortedURL',
        ),
    ]
