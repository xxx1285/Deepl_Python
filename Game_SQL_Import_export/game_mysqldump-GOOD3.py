

# import os
import json
import subprocess


# куди зберігаємо SQL файл
output_file = r'Game_SQL_Import_export\baza\test_3.sql'

# SQL Зчитуємо параметри з конфігураційного файлу
with open(r'Game_SQL_Import_export\configs\config_sql_import_export.json', 'r') as f:
    config = json.load(f)

# Експорт таблиць
my_tables = ['modx_categories', 'modx_context', 'modx_context_setting',
             'modx_media_sources_elements', 'modx_migx_configs',
             'modx_migx_formtabs', 'modx_migx_formtab_fields',
             'modx_site_content', 'modx_site_htmlsnippets', 'modx_site_templates',
             'modx_site_tmplvars', 'modx_site_tmplvar_contentvalues',
             'modx_site_tmplvar_templates', 'modx_system_settings']

# my_tables_str = ", ".join(my_tables)


host = config['export_1']['host']
user = config['export_1']['user']
password = config['export_1']['password']
database = config['export_1']['database']
dump_file = 'dump333.sql'

# Создание команды для mysqldump
command = f"mysqldump -h {host} -u {user} -p{password} {database} " + " ".join(my_tables) + f" > {dump_file}"

# # Ввод пароля
# password = getpass.getpass("Введите пароль для пользователя {user}: ")

# # Создание команды для mysqldump
# command = ["mysqldump", "--host", host, "--user", user, f"--password={password}", database] + my_tables
# command += ["--result-file", dump_file]


# # Запуск команды и сохранение вывода в файл
# with open(dump_file, 'w') as f:
#     subprocess.run(command, shell=True, stdout=f, check=True)
#     print('ok')

with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    try:
        proc.wait(timeout=30)
    except subprocess.TimeoutExpired:
        proc.kill()
        _, error = proc.communicate()
        print(f"Process killed due to timeout: {error.decode('unicode_escape').encode('utf-8')}")
    else:
        if proc.returncode == 0:
            print("Success")
        else:
            _, error = proc.communicate()
            print(f"Error: {error.decode('cp1252')}")
