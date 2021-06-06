from django.shortcuts import render

from django.http import HttpResponse, response
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

import csv
from .models import TcsiElement

# Create your views here.
def logoutuser(request):
    logout(request)
    return redirect("https://www.tsheringwangchen.net")

def index(request):
    return render(request, 'tcsiapp/index.html')

def tcsielement(request):
    tcsi_list = TcsiElement.objects.all()
    context = {'tcsi_list': tcsi_list}
    return render(request, 'tcsiapp/tcsielement.html', context)

def downloadcsv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename = "tcsi_elements.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'element_no',
        'page_title',
        'description',
        'code_category',
        'element_type',
        'width',
        'version_revision_date',
        'version',
        'years_version_active',
        'sub_header',
        'value',
        'meaning',
        'derivation',
        'spec_flag',
        'retired',
        'page_access_timestamp',
        'page_url',
        'page_harvestor'
    ])

    for row in TcsiElement.objects.all():
        writer.writerow([
            row.element_no,
            row.page_title,
            row.description,
            row.code_category,
            row.element_type,
            row.width,
            row.version_revision_date,
            row.version,
            row.years_version_active,
            row.sub_header,
            row.value,
            row.meaning,
            row.derivation,
            row.spec_flag,
            row.retired,
            row.page_access_timestamp,
            row.page_url,
            row.page_harvestor
        ])
    return response
