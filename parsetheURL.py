from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import requests
import pandas as pd
import re
from createSchemaAdobe import createSchemaAdobe
from createSchemaMongo import createSchemaMongo
from createSchemaGeneral import createSchemaGeneral
from urllib.parse import urlsplit
import datetime
import time


def parsetheURLPage(url): 
    html = requests.get(url).content
    df_list = pd.read_html(html)
    # print(type(df_list), len(df_list))
    secdf=""
    for df in df_list:
        for df1 in df:
            if "CVE".lower() in df1.lower():
                secdf = df
                break
    
    if type(secdf)==str:
        print("No CVE table found in the url:", url)
        exit(1)

    base_url = "{0.netloc}/".format(urlsplit(url))
    # print(base_url)
    vendor = base_url.split(".")[1:-1][-1]
    print("vendor: {}".format(vendor))

    # df = df_list[-1]
    listobj = secdf.values.tolist()
    if vendor == "mongodb":
        return createSchemaMongo(listobj, vendor, url)
    if vendor == "adobe":
        return createSchemaAdobe(listobj, vendor, url)
    else:
        return createSchemaGeneral(listobj, vendor, url)




