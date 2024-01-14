from llama_cpp import Llama

def app_llama(model, title, text_game):
    prompt = "Напиши краткий обзор товара '" + title + "'. Характеристики товара '" + title + "': " + text_game
    output = model(prompt, max_tokens=700, echo=False)
    result_lama_text_game = output['choices'][0]['text']
    index = result_lama_text_game.find(".")
    result_lama_text_game = result_lama_text_game[index + 2:]

    return result_lama_text_game