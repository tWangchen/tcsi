from rest_framework import serializers
from tcsiapp.models import TcsiElement


class TcsiElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TcsiElement
        fields = ["element_no", "page_title", "description", "code_category", "element_type", "width", "version_revision_date", 
            "version", "years_version_active", "sub_header", "value", "meaning", "derivation", "spec_flag", "retired", "page_access_timestamp", "page_url", "page_harvestor"
        ]