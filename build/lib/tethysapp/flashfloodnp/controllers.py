from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import decimal, csv, json
from .chartUtils import getForecastData, get_forecastpercent
import requests, psycopg2
from datetime import timedelta
import datetime as dt
# from .utils import get_thredds_info
from .config import APIHost, AuthorizationToken

def check_for_decimals(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError

def getRecentDate(comid, cty):
    # conn = psycopg2.connect(host="192.168.10.163", database="servirFloodHiwat", user="servirData", password="m2caab5h3BwX")
    conn = psycopg2.connect(host="192.168.10.163", database="GEOGloWS_V2_HIWAT", user="postgres", password="Changeit3#")
    cur = conn.cursor()
    query = 'select distinct(rundate) from public.forecast' + cty + ' where comid = ' + comid + ' order by rundate desc'

    try:
        cur.execute(query)
        a = cur.fetchall()
        bb = (str(a[0])[19:-3]).split(",")
        b = bb[0].strip() + "-" + "{:02d}".format(int(bb[1])) + "-" + "{:02d}".format(int(bb[2]))
    except:
        runDate = dt.datetime.now().date() - timedelta(1)
        b = runDate.strftime('%Y-%m-%d')

    conn.close()
    return b

def getGeoJson(loc):
    request_params = dict(cty=loc)
    request_headers = dict(Authorization=AuthorizationToken)
    res = requests.get(APIHost+'/apps/apicenter/hiwatAPI/getFeaturesHIWATPA', params=request_params,headers=request_headers)
    # print (res.text)
    return(res.text)

def getGeoJson1(request):
    loc = request.GET.get('stID').strip()
    request_params = dict(cty=loc)
    request_headers = dict(Authorization=AuthorizationToken)
    res = requests.get(APIHost+'/apps/apicenter/hiwatAPI/getFeaturesHIWATPA', params=request_params,headers=request_headers)
    # print (res.text)
    # return(res.text)
    return HttpResponse(res.text, content_type='application/json')

def chartHiwat(request):
    return_obj = {}
    try:
        comid =int(request.GET.get('stID'))
        dateComplete=request.GET.get('date')
    except:
        comid = 57465
        dateComplete=None

    return_obj = getForecastData(comid,dateComplete)

    # print (return_obj)
    return HttpResponse(return_obj, content_type= 'application/json')

def forecastpercent(request):
    if request.is_ajax() and request.method == 'GET':
        comid = request.GET.get('comid')
        return JsonResponse(get_forecastpercent(comid))

def home(request):
    # getjson = getGeoJson('Babai')
    # thredds_wms_obj = get_thredds_info()
#    print(getjson)
    context = {
        # 'myJson': getjson,
        # 'thredds_urls': json.dumps(thredds_wms_obj),
    }
    return render(request, 'flashfloodnp/main.html', context)

def getForecastCSV(request):
    comid = request.GET.get('comid')
    cty = request.GET.get('cty')
    recentDate = request.GET.get('forecastDate')
    if recentDate is None:
        recentDate = getRecentDate(comid, cty)
    # conn = psycopg2.connect(host="192.168.10.163", database="servirFloodHiwat", user="servirData", password="m2caab5h3BwX")
    conn = psycopg2.connect(host="192.168.10.163", database="GEOGloWS_V2_HIWAT", user="postgres", password="Changeit3#")
    cur = conn.cursor()
    query = "SELECT forecastdate, forecastvalue FROM public.forecast" + cty + " where comid =" \
            + str(comid) + " and runDate = '" + str(recentDate) + "' order by forecastdate"

    cur.execute(query)
    rows = cur.fetchall()
    # // CSV starts herer
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="forecastData_' + str(comid) + '.csv"'
    header = ['Dates', 'Values']
    writer = csv.writer(response)
    writer.writerow(header)

    for row in rows:
        dates = (str(dt.datetime.strftime(row[0], '%Y-%m-%d %H:%M:%S')))
        values = (float(row[1]))

        writer.writerow([dates, values])
    conn.close()
    return response

def getHistoricCSV(request):
    comid = request.GET.get('comid')
    cty = request.GET.get('cty')

    # conn = psycopg2.connect(host="192.168.10.163", database="servirFloodHiwat", user="servirData", password="m2caab5h3BwX")
    conn = psycopg2.connect(host="192.168.10.163", database="GEOGloWS_V2_HIWAT", user="postgres", password="Changeit3#")
    cur = conn.cursor()
    # query = "select historydate, historyvalue from history" + cty + " where comid = " + str(
    #     comid) + " order by historydate"
    query = f"select historydate, historyvalue from historic.history{cty}_{str(comid)}"
    cur.execute(query)
    rows = cur.fetchall()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="historicData_' + str(comid) + '.csv"'
    header = ['Dates', 'Values']
    writer = csv.writer(response)
    writer.writerow(header)
    for row in rows:
        mydate = str(dt.datetime.strftime(row[0], '%Y-%m-%d %H:%M:%S'))
        writer.writerow([mydate, row[1]])
    conn.close()
    return response
