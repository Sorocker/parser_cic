import requests
from bs4 import BeautifulSoup
import json

url = 'https://myciclon.com/shop/'
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

ul_tag = soup.select('ul[class="product-categories"] > li > a')

for a_tag in ul_tag:
    if not a_tag['href'].__contains__("stok-moskva"):
        categ_url = a_tag['href']
        response = requests.get(categ_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.find('h1'))
        cat_ul_tag = soup.select('ul[class="products columns-4"] > li > a')
        for cat_a_tag in cat_ul_tag:
            jewelry_url = cat_a_tag['href']
            response = requests.get(jewelry_url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            print(cat_a_tag['href'])
            jsn = None
            img_href = ""

            try:
                jsn = soup.find(class_="variations_form")['data-product_variations']
            except Exception:
                img_href = soup.find('figure', {"class": "woocommerce-product-gallery__wrapper"}).find('div').find('a')[
                    'href']
                print(img_href)
                print("One product variation")

            if jsn:
                for image in json.loads(jsn):
                    print(image['image']['url'])
            # Находим тег select
            # select_tag = soup.find('select', {"id": "pa_color"})
            # if select_tag:
            #     # Получаем значение из тега select
            #     options = select_tag.find_all('option')
            #     print(options)
            #     for option in options:
            #         value = option.get('value')
            #         # print(value)
            #         # Отправляем post запрос с полученным значением
            #         payload = {'pa_color': value}
            #         print(payload)
            #         r = requests.post(jewelry_url, data=payload, headers=headers)
            #         # Используем BeautifulSoup для парсинга полученного HTML
            #         get_options_soup = BeautifulSoup(r.text, 'html.parser')
            #         option_id = ''
            #         value.join(filter(str.isdigit, option_id))
            #         # Находим все теги img с role="presentation" и скачиваем картинки
            #         img_tags = get_options_soup.find('figure', {"class": "woocommerce-product-gallery__wrapper"}).find('div').find('a')['href']
            #         print(img_tags)
            #         for img_tag in img_tags:
            #             pass
                        # img_url = img_tag['href']
                        # print(img_url)
                        # ВЫТАЩИТЬ СРЦ ИЗ ИМДЖ, ИМДЖ НЕ НАХОДИТ
                        # print(img_tag['href'])
                        # img_response = requests.get(img_url)
                        # img_name = urlparse(img_url).path.split('/')[-1].replace(".jpg", "") + "_" + value
                        # print(img_name)
                        # with open(img_name + "_" + value + ".jpg", 'wb') as f:
                        #     f.write(img_response.content)
