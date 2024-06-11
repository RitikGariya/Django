from django.db import models

# Create your models here.
class FirmDetails(models.Model):
    firm_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    gstn_no = models.CharField(max_length=15)
    msme_status = models.BooleanField(default=False)
    certification_name = models.CharField(max_length=255, blank=True, null=True)
    firm_pdf = models.FileField(upload_to="pdf/")

    def __str__(self):
        return self.firm_name