import os
import time


def delete_files_from_list(delete_list_path, base_path):
    with open(delete_list_path, "r") as file:
        paths = file.readlines()

    for relative_path in paths:
        relative_path = relative_path.strip()
        full_path = os.path.join(base_path, relative_path)

        attempts = 0
        max_attempts = 30
        while attempts < max_attempts:
            try:
                if os.path.exists(full_path):
                    os.remove(full_path)
                break
            except PermissionError:
                time.sleep(1)
                attempts += 1
    # Очистка текстового файла после удаления всех файлов
    with open(delete_list_path, "w") as file:
        pass  # Открытие файла в режиме 'w' автоматически очищает его содержимое

# delete_list_path = "paths_to_delete.txt"
# base_path = "/путь/к/вашему/корневому/каталогу/проекта"  # Замените на нужный базовый путь
# delete_files_from_list(delete_list_path, base_path)


# # ЯКЩО САМОСТЫЙНО ВИДАЛИТИ ПОТРЫБНО
# delete_list_path = "C:/Gembling/Deepl_Python/Deepl_Python/VideoRec_from_SiteMonitor/2_Scrin_Video_PragmatPlayGames/output/video_to_delete.txt"
# base_path_del = "C://Gembling//Deepl_Python//Deepl_Python//"
# try:
#     delete_files_from_list(delete_list_path, base_path_del)
# except Exception as e:
#     print(f"Произошла ошибка при удалении файлов: {e}")
