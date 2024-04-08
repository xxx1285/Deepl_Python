import xml.etree.ElementTree as ET
from datetime import datetime

def generate_and_save_sitemap(urls, output_file):
    # Создаем корневой элемент <urlset>
    root = ET.Element("urlset")
    root.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    # Получаем текущую дату и время в формате ISO 8601
    current_time = datetime.now().replace(microsecond=0).isoformat()  # Убираем микросекунды
    
    
    # Создаем элементы <url> для каждого URL-адреса
    for url in urls:
        url_element = ET.SubElement(root, "url")
        
        loc_element = ET.SubElement(url_element, "loc")
        loc_element.text = url
        
        # Добавляем элемент lastmod с текущей датой и временем
        lastmod_element = ET.SubElement(url_element, "lastmod")
        lastmod_element.text = current_time
        
        # Можно добавить другие элементы, такие как changefreq, priority, если нужно
        
    # Создаем XML дерево
    tree = ET.ElementTree(root)
    
    # Сохраняем XML дерево в файл
    tree.write(output_file, encoding="UTF-8", xml_declaration=True)