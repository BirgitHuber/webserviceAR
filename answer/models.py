from __future__ import unicode_literals

from django.db import models


# defines the relation in the database
class Code(models.Model):
    # object code  -> barcode
    code = models.CharField(max_length=100)
    object_type = models.CharField(max_length=500)
    info_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.code

