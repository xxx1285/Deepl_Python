import requests
import xml.etree.ElementTree as ET
import json

def parse_xml_from_web(url, user_agent, json_file):
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        xml_data = response.content
        root = ET.fromstring(xml_data)

        categories = {}
        for category in root.find('shop').find('categories').findall('category'):
            category_id = category.get('id')
            category_parentId = category.get('parentId')
            if category_parentId:
                categories[category_parentId] = category_id
                # categories[category_id] = category_parentId

        offers = []

        # Находим <offers> и проходим по его дочерним элементам
        for offer in root.find('shop').find('offers').findall('offer'):
            offer_data = {}
            offer_data['id'] = offer.get('id')
            offer_data['categoryId'] = int(offer.find('categoryId').text)
            # Получаем родительскую категорию, если она существует
            category_lvl2 = categories.get(str(offer_data['categoryId']), None)
            offer_data['category_lvl2'] = category_lvl2

            offer_data['group_id'] = offer.get('group_id')  # Получаем group_id
            offer_data['url'] = offer.find('url').text
            offer_data['price'] = int(offer.find('price').text)
            offer_data['oldprice'] = int(offer.find('price').text)
            offer_data['currencyId'] = offer.find('currencyId').text
            offer_data['pictures'] = [pic.text for pic in offer.findall('picture')]
            offer_data['store'] = offer.find('store').text == 'true'
            offer_data['pickup'] = offer.find('pickup').text == 'true'
            offer_data['delivery'] = offer.find('delivery').text == 'true'
            offer_data['name'] = offer.find('name').text
            offer_data['vendor'] = offer.find('vendor').text
            offer_data['vendorCode'] = offer.find('vendorCode').text
            offer_data['model'] = offer.find('model').text
            offer_data['description'] = offer.find('description').text
            offer_data['manufacturer_warranty'] = offer.find('manufacturer_warranty').text == 'true'

            params = {}
            for param in offer.findall('param'):
                param_name = param.get('name')
                param_value = param.text
                params[param_name] = param_value
                if param_name.startswith("Розмір матрацу"):
                    offer_data['rozmir'] = param_value
            offer_data['params'] = params

            offers.append(offer_data)

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(offers, f, ensure_ascii=False, indent=4)
    else:
        print("Failed to fetch data from the URL")

if __name__ == "__main__":
    url = "https://matroluxe.ua/index.php?route=extension/feed/yandex_yml3"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    json_file = r"Parsing\Parsing_Matrolux\output\output_json_file3.json"
    parse_xml_from_web(url, user_agent, json_file)