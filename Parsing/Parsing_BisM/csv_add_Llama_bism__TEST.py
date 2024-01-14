import os
import json
import pandas as pd

from llama_cpp import Llama


CSV_FILE = r"Parsing\Parsing_BisM\CSV\result5.csv"
CSV_RESULT = r"Parsing\Parsing_BisM\CSV\result5-2.csv"

MODEL_LLAMA_PATH = "D://Gembling//Deepl_Python//Deepl_Python//llama//TheBloke//llama-2-7b-chat.Q5_K_S.gguf"
model_Llama = Llama(model_path=MODEL_LLAMA_PATH, n_ctx=1048)


def app_llama(model, title, text_game):
    prompt = "Напиши текст про: '" + text_game + "' для товара '" + title + "'. Текст должен быть на руском языке"
    output = model(prompt, max_tokens=500, echo=False)
    result_lama_text_game = output['choices'][0]['text']
    index = result_lama_text_game.find(".")
    result_lama_text_game = result_lama_text_game[index + 2:]

    return result_lama_text_game


def process_technical_info(model, title, technical_info):
    # Разбиваем информацию на строки
    lines = technical_info.split('\n')
    processed_lines = [app_llama(model, title, line) for line in lines if line.strip()]
    # Объединяем обработанные строки в одну статью
    full_article = ' '.join(processed_lines)
    return full_article

def process_csv(file_path, model):
    df = pd.read_csv(file_path, sep=';')
    # Обрабатываем каждую строку в DataFrame
    df['ai_llama'] = df.apply(lambda row: process_technical_info(model, row['title'], row['technical_info']), axis=1)
    return df


def main():
    processed_df = process_csv(CSV_FILE, model_Llama)
    processed_df.to_csv(CSV_RESULT, sep=';', index=False)

if __name__ == '__main__':
    main()
