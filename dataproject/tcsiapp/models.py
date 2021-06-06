from django.db import models

class TcsiElement(models.Model):
    id = models.IntegerField(primary_key=True)
    element_no = models.CharField(max_length=255, blank=True, null=True)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    code_category = models.CharField(max_length=255, blank=True, null=True)
    element_type = models.CharField(max_length=255, blank=True, null=True)
    width = models.CharField(max_length=255, blank=True, null=True)
    version_revision_date = models.CharField(max_length=255, blank=True, null=True)
    version = models.CharField(max_length=255, blank=True, null=True)
    years_version_active = models.CharField(max_length=255, blank=True, null=True)
    sub_header = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    meaning = models.CharField(max_length=5000, blank=True, null=True)
    derivation = models.CharField(max_length=255, blank=True, null=True)
    spec_flag = models.CharField(max_length=255, blank=True, null=True)
    retired = models.CharField(max_length=255, blank=True, null=True)
    page_access_timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    page_url = models.CharField(max_length=255, blank=True, null=True)
    page_harvestor = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tcsi_element'
