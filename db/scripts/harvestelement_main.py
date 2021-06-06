"""Purpose: To automate TCSI open web data harvesting due to lack of standard api
Author: TW
"""
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import csv
import time
import random
import re
import psycopg2
from psycopg2.extras import execute_values

from harvestelementid import DataElement

def main():
    try:
        wait_min = 10  # Defines min random wait time(in seconds) before extraction
        wait_max = 40  # Defines max random wait time(in seconds) before extraction
        base_url = "https://www.tcsisupport.gov.au/element/"
        now = datetime.now()
        element = []
        page_harvestor = "tWangchen" 
        pgconn = None
        logger = (f"Hi {page_harvestor}, recorded below are your logs from today {now.date()}\n")
      
        # Start element_num for loop
        for elementid in DataElement().element_number():
            element_num = elementid['ELEMENT_ID'].strip()
            url = f"{base_url}{element_num}"
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    time.sleep(random.randint(wait_min, wait_max))  # Add random wait time before extraction
                    webcontent = BeautifulSoup(response.content, "lxml")
                    # Start extracting webcontent.
                    # Important note: if the output is unexpected, likely the webcontent have changed,
                    # in which case try updating the target definition(s) below.
                    title = webcontent.find('h1').text
                    description = webcontent.find('div', class_='field field--name-field-description field--type-string-long field--label-hidden field__item').text
                    code_category = webcontent.find('div', class_='field field--name-field-code-category field--type-entity-reference field--label-inline').find('div', class_='field__item').text
                    element_no = webcontent.find('div', class_='field field--name-field-code field--type-integer field--label-inline').find('div', class_='field__item').text
                    element_type = webcontent.find('div', class_='block block-ctools-block block-entity-fieldnodefield-element-type').find('div', class_='field__item').text
                    width = webcontent.find('div', class_='block block-ctools-block block-entity-fieldnodefield-data-size').find('div', class_='field__item').text
                    ver_rev_date = webcontent.find('div', class_='block block-ctools-block block-entity-fieldnodefield-version-revision-date').find('div', class_='field__item').text
                    version = webcontent.find('div', class_='block block-ctools-block block-entity-fieldnodefield-version').find('div', class_='field__item').text
                    yrs_ver_active = webcontent.find('div', class_='block block-ctools-block block-entity-fieldnodefield-years').find('div', class_='field__item').text
                    retired = webcontent.find('div', class_='validity-699')
                    tables = webcontent.find_all('table')
                    # End extracting webcontent
                    
                    # Start core data requirements logic
                    # Retired condition may be redundant as Data Element Dictionaly table(https://www.tcsisupport.gov.au/elements) appears to only have active elements; 
                    # need further review of elements.

                    if tables:
                        for table in tables:
                            table_title = table.find_previous(re.compile("^h")).text
                            for tr in table.find_all('tr')[1:]:
                                td = tr.find_all('td')
                                td_length = len(td)
                                print(f"\nProcessing HEIMS_E{element_num}: current table have {td_length} table columns; if table columns are more than 3, please investigate further.")
                                logger += (f"\nProcessing HEIMS_E{element_num}: current table have {td_length} table columns; if table columns are more than 3, please investigate further.")
                                if td_length == 3:
                                    spec = {
                                        "element_no" : element_no,
                                        "page_url" : url,
                                        "page_title" : title,
                                        "page_access_timestamp" : now,
                                        "page_harvestor" : page_harvestor,
                                        "description" : description,
                                        "code_category" : code_category,
                                        "element_type" : element_type,
                                        "width" : width,
                                        "version_revision_date" : ver_rev_date,
                                        "version" : version,
                                        "years_version_active" : yrs_ver_active,
                                        "sub_header" : table_title,
                                        "value" : td[0].text,
                                        "meaning" : td[1].text,
                                        "derivation" : td[2].text,
                                        "spec_flag" : "Y",
                                        "retired" : "N"
                                    }                                    
                                    element.append(spec)
                                else:  # Intentionally left without condition, so everything outside 3 columns will at least have two columns processed
                                    spec = {
                                        "element_no" : element_no,
                                        "page_url" : url,
                                        "page_title" : title,
                                        "page_access_timestamp" : now,
                                        "page_harvestor" : page_harvestor,
                                        "description" : description,
                                        "code_category" : code_category,
                                        "element_type" : element_type,
                                        "width" : width,
                                        "version_revision_date" : ver_rev_date,
                                        "version" : version,
                                        "years_version_active" : yrs_ver_active,
                                        "sub_header" : table_title,
                                        "value" : td[0].text,
                                        "meaning" : td[1].text,
                                        "derivation" : "",
                                        "spec_flag" : "Y",
                                        "retired" : "N"
                                    }                                    
                                    element.append(spec)
                    else:
                        nospec = {
                            "element_no" : element_no,
                            "page_url" : url,
                            "page_title" : title,
                            "page_access_timestamp" : now,
                            "page_harvestor" : page_harvestor,
                            "description" : description,
                            "code_category" : code_category,
                            "element_type" : element_type,
                            "width" : width,
                            "version_revision_date" : ver_rev_date,
                            "version" : version,
                            "years_version_active" : yrs_ver_active,
                            "sub_header" : "",
                            "value" : "",
                            "meaning" : "",
                            "derivation" : "",
                            "spec_flag" : "N",
                            "retired" : "N"
                        }                                    
                        element.append(nospec)
                    print(f"\nProcessed HEIMS_E{element_num}")
                    logger += (f"\nProcessed HEIMS_E{element_num}")
                    # End core data requirements logic
                except Exception as error_msg:
                    print(f"\n\nError processing HEIMS_E{element_num}: {error_msg}\n")
                    logger += (f"\n\nError processing HEIMS_E{element_num}: {error_msg}\n")
            else:
                print(f"\n\nURL: {url}\n Response code: {response.status_code}\n")
                logger += (f"\n\nURL:{url}\n Response code: {response.status_code}\n")
        # End element_num for loop

        # Send data to DB
        pgconn = psycopg2.connect("dbname='Intentionally removed' user='Intentionally removed' host='Intentionally removed' password='Intentionally removed'")
        if(pgconn):
            pgcur = pgconn.cursor()
            pgcur.execute('TRUNCATE TABLE tcsi_element CASCADE')
            tcsiquery = "INSERT INTO tcsi_element(\
                                element_no,\
                                page_title,\
                                description,\
                                code_category,\
                                element_type,\
                                width,\
                                version_revision_date,\
                                version,\
                                years_version_active,\
                                sub_header,\
                                value,\
                                meaning,\
                                derivation,\
                                spec_flag,\
                                retired,\
                                page_access_timestamp,\
                                page_url,\
                                page_harvestor\
                            )\
                            VALUES(\
                                %(element_no)s,\
                                %(page_title)s,\
                                %(description)s,\
                                %(code_category)s,\
                                %(element_type)s,\
                                %(width)s,\
                                %(version_revision_date)s,\
                                %(version)s,\
                                %(years_version_active)s,\
                                %(sub_header)s,\
                                %(value)s,\
                                %(meaning)s,\
                                %(derivation)s,\
                                %(spec_flag)s,\
                                %(retired)s,\
                                %(page_access_timestamp)s,\
                                %(page_url)s,\
                                %(page_harvestor)s\
                            )\
                        "        
            pgcur.executemany(tcsiquery, element)
            pgconn.commit()
            pgcur.close()
        else:
            print(f"\n\nSomething is wrong with pg connection\n")
            logger += (f"\n\nSomething is wrong with pg connection\n")

        print(f"\n\nDone.")
        logger += (f"\n\nDone.")            

    except Exception as e:
        logger = (f"\n Error message: {e}")
    finally:
        if pgconn is not None:
            pgconn.close()
        # This will write to a log file
        f = open(f"tcsiharvest_{now.date()}.log", 'a')
        f.write(f"{logger}")
        f.close()
            
if __name__ == '__main__':
    main()
