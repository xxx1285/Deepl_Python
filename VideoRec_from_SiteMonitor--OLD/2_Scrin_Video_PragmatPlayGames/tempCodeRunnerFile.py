    try:
        delete_files_from_list(delete_list_path, base_path_del)
    except Exception as e:
        print(f"Произошла ошибка при удалении файлов: {e}")