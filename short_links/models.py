from django.db import models
from django.db.models import Index, UniqueConstraint


# Create your models here.


class LinkStorage(models.Model):
    original_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=25)

    class Meta:
        Index('code', 'original_link', name='code_original_link_index')
        UniqueConstraint(fields=["code"], name="unique_code")
