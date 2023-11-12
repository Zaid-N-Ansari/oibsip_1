from django.db import models
from uuid import uuid4

class CalcHist(models.Model):
    hist = models.CharField(max_length=18)
    hist_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
