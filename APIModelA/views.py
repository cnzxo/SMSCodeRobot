from bs4 import BeautifulSoup
from django.http import HttpResponse, JsonResponse

# Create your views here.
from APIModelA.common import http_request_get


def index(request):
    return HttpResponse('ok')


def countries(request):
    url = 'https://sms24.info/en/countries/'
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, 'html.parser')
    html_div = soup.select('.card .container-fluid>.row')[0]
    html_list = html_div.select('div>a')
    res_list = []
    for html_list_item in html_list:
        img_path = html_list_item.select('img')[0]['src']
        img_name = img_path[img_path.rfind('/') + 1:]
        res_item_href = html_list_item['href'].split('/')
        res_item_href = [var for var in res_item_href if var]
        res_item = {
            'country': html_list_item.text.strip(),
            'code': res_item_href[len(res_item_href) - 1].strip(),
            'image': '/static/img/{}'.format(img_name.strip()),
        }
        res_list.append(res_item)

    return JsonResponse(res_list, safe=False)


def numbers(request):
    url = 'https://sms24.info/en/numbers/'
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, 'html.parser')
    html_list = soup.select('.card .container-fluid>.row div>a')
    res_list = []
    for html_list_item in html_list:
        res_item_img = html_list_item.select('img')[0]['src'].strip()
        res_item_country = html_list_item.select('h5')[0].text.strip()
        res_item_number = html_list_item.select('div')[0].text.strip()
        res_list_item = {
            'image': '/static/img/{}'.format(res_item_img[res_item_img.rfind('/') + 1:]),
            'country': res_item_country,
            'number': res_item_number.removeprefix('+'),
        }
        res_list.append(res_list_item)

    return JsonResponse(res_list, safe=False)


def numbers_by_country(request, country):
    url = 'https://sms24.info/en/countries/{}/'.format(country)
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, 'html.parser')
    html_div = soup.select('.card .container-fluid>.row')[0]
    html_list = html_div.select('div>a')
    res_list = []
    for html_list_item in html_list:
        res_item_img = html_list_item.select('img')[0]['src'].strip()
        res_item_country = html_list_item.select('h5')[0].text.strip()
        res_item_number = html_list_item.select('div')[0].text.strip()
        res_item = {
            'image': '/static/img/{}'.format(res_item_img[res_item_img.rfind('/') + 1:]),
            'country': res_item_country,
            'number': res_item_number.removeprefix('+'),
        }
        res_list.append(res_item)

    return JsonResponse(res_list, safe=False)


def messages_by_number(request, number):
    url = 'https://sms24.info/en/numbers/{}/'.format(number)
    print(url)
    html = http_request_get(url)
    if html.status_code != 200:
        return HttpResponse('Request failure.')
    soup = BeautifulSoup(html.text, 'html.parser')
    html_list = soup.select('.card .container-fluid>.row>.col-12')
    res_list = []
    for html_list_item in html_list:
        res_item_time = html_list_item.select('div.text-muted')[0]['data-created'].strip()
        res_item_time = res_item_time[:res_item_time.rfind('.')].replace('T', ' ')
        res_item_from = html_list_item.select('.callout span>a')[0].text.strip()
        res_item_message = html_list_item.select('.callout span')[3].text.strip()
        res_item = {
            'time': res_item_time,
            'from': res_item_from,
            'message': res_item_message,
        }
        res_list.append(res_item)

    return JsonResponse(res_list, safe=False)
