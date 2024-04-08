from llama_cpp import Llama

MODEL_LLAMA_PATH = "D://Gembling//Deepl_Python//Deepl_Python//llama//TheBloke//llama-2-7b-chat.Q5_K_S.gguf"
model_Llama = Llama(model_path=MODEL_LLAMA_PATH, n_ctx=2048)

def app_llama(model, text_game):
    prompt = "Rewrite this text into an article in English as if you personally played this game, don't comment on the task but only write the article and insert positive emotions, don't use emoji and special characters: " + text_game
    output = model(prompt, max_tokens=500, echo=False)
    result_lama_text_game = output['choices'][0]['text']
    index = result_lama_text_game.find(".")
    result_lama_text_game = result_lama_text_game[index + 2:]

    return result_lama_text_game