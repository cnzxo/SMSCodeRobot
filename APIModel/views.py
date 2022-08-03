import re
import time

from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse

# Create your views here.
from APIModel.common import http_request_get


def index(request):
    return HttpResponse('Hello, SMS Code Robot! Time:{}'.format(time.time()))


def countries(request):
    url = 'https://smsreceivefree.com/'
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, "html.parser")
    link_list = soup.select('.button-clear')
    res_list = []
    for link in link_list:
        value = link['href'][link['href'].rfind('/') + 1:]
        res_link = {'value': value, 'title': link.text}
        res_list.append(res_link)
    return JsonResponse(res_list, safe=False)


def numbers(request):
    country = 'usa'
    if request.GET.get('country'):
        country = request.GET.get('country')
    url = 'https://smsreceivefree.com/country/' + country
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, 'html.parser')
    phone_info_list = soup.select('.container .numview')
    res_list = []
    for phone_info in phone_info_list:
        phone_desc = phone_info.select('small')
        phone_num = phone_info.select('.numbutton')
        phone_paras = re.split(r'[(|)]', phone_num[0].text)
        phone_paras = [var for var in phone_paras if var]
        res_list_item = {'address': phone_desc[0].text.strip(), 'time': phone_desc[1].text.strip(),
                         'phone': phone_paras[0].strip().removeprefix('+'), 'count': phone_paras[1].strip()}
        res_list.append(res_list_item)
    return JsonResponse(res_list, safe=False)


def info(request):
    if not request.GET.get('number'):
        return HttpResponse('Missing parameter number.')
    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')
    number = request.GET.get('number')
    url = 'https://smsreceivefree.com/info/{}/?page={}'.format(number, page)
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    if html.text.find('Number Removed') > 0:
        return HttpResponse("The number does not exist.")
    soup = BeautifulSoup(html.text, 'html.parser')
    table = soup.select('.messagesTable2')[0]
    tbody = table.select('tbody')[0]
    tbody_tr = tbody.select('tr')
    res_list = []
    for tr in tbody_tr:
        td = tr.select('td')
        td_from = td[0].text.split('\n')
        td_from = [var for var in td_from if var]
        td_message = td[1]
        res_item = {'number': td_from[0].strip(), 'time': td_from[1].strip(), 'message': td_message.text.strip()}
        res_list.append(res_item)

    return JsonResponse(res_list, safe=False)
