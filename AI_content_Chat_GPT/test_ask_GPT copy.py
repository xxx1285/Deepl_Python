import openai
import json
import io
from PyPDF2 import PdfFileWriter, PdfFileReader
from datetime import datetime

# Загружаем параметры из конфигурационного файла
with open(r'AI_content_Chat_GPT\config\config_OpenAi_Key.json') as f:
    config = json.load(f)
openai.api_key = config['config_openai']['api_openai_key']

# Запрос к OpenAI
prompt = "write name first king in GB"
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5,
)

# Получаем ответ и убираем лишние символы
text = response.choices[0].text.strip()

# Создаем PDF с полученным текстом
pdf_writer = PdfFileWriter()
pdf_writer.addBlankPage(width=72*8.5, height=72*11)
pdf_page = pdf_writer.getPage(0)
pdf_page.setFillColorRGB(0, 0, 0)
pdf_page.setFontSize(12)
pdf_page.beginText(72, 72*10)
pdf_page.insertText(text)
pdf_page.endText()
pdf_writer.addPage(pdf_page)

# Создаем название файла с текущей датой и временем
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f'First_King_GB_{current_datetime}.pdf'

# Записываем PDF-документ в файл
with open(file_name, 'wb') as output_pdf:
    pdf_writer.write(output_pdf)

print(f'PDF-документ сохранен под именем {file_name}')
