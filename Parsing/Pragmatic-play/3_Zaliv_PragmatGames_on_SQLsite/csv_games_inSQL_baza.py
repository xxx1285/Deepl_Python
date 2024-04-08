import csv
import pymysql
import json
import os
import time
import random

from app.app_perefraziruem_text_NLTK_SpaCy import paraphrase_with_spacy


# SQL Config path
sql_config = r'Parsing\Pragmatic-play\3_Zaliv_PragmatGames_on_SQLsite\configs\config_sql.json'
with open(sql_config, 'r') as f:
    configSQL = json.load(f)
# Открываем CSV файл
csv_file_path = r'Parsing\Pragmatic-play\3_Zaliv_PragmatGames_on_SQLsite\input\output-urls-games-14-02-2024-v3.csv'


try:
    # Подключаемся к базе данных
    connect_database = pymysql.connect(**configSQL['config_database'],
                                       port=3306,
                                       cursorclass=pymysql.cursors.DictCursor)
    with connect_database.cursor() as cursor:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                # EDIT TITLE и другие
                title_random_key = random.choice(['real money slot', 'real money game', 'online slot', 'online game', 
                                                  'online bet slot', 'best slot in 2024', 'game download', 'slot download', 
                                                  'casino online slot', 'casino online game', 'official website', 
                                                  'casino slot', 'login online', 'online play slot'])
                new_pagetitle = f"{row['title_game']} 1win"

                search_strings = ["Scratchcard", "Roulette", "Blackjack"]
                if any(s in row['title_game'] for s in search_strings):
                    new_longtitle = f"{row['title_game']} 1win"
                else:
                    new_longtitle = f"{row['title_game']} 1win {title_random_key}"
                text_game_NLTK = paraphrase_with_spacy(row['text_game'])

                #####################################################################
                # CONTENT JSON
                #####################################################################
                # Разделение текста на абзацы
                abzats = row['text_game_Llama_1000_and_nachalo'].split('\n')
                # Использование первой строки для "h2_title"
                b1_content_json_h2_title = abzats[0]
                # Оборачивание оставшихся абзацев в теги <p>
                b1_content_json_description_abzats = ['<p>' + p.replace('\n', '') + '</p>' for p in abzats[1:] if p]
                # Создание JSON структуры
                json_structure = [{
                    "MIGX_id": "1",
                    "h2_title": b1_content_json_h2_title,
                    "SEO_id_h2_title": "1win-portal-betting",
                    "description": "\n\n".join(b1_content_json_description_abzats),
                    "alt_img": b1_content_json_h2_title,
                    "image": "games/" + row['image_1']
                }]
                # Конвертация в JSON строку
                b1_content_json= json.dumps(json_structure, indent=4)
                #####################################################################
                # Создаем JSON массив для image_galer_json
                image_galer_json_list = []
                for i in range(1, 7):
                    image_galer_json_list.append({
                        "MIGX_id": str(i),
                        "description": f"image slot {row['title_game']} - {i} play",
                        "image": f"games/{row['alias']}/images/image-slot-{row['alias']}-{i}.jpg"
                    })
                image_galer_json = json.dumps(image_galer_json_list)

                img_mini = f"games/{row['alias']}/images/image-slot-{row['alias']}-480x.webp"

                # SQL tables
                resource_id     = 484
                pagetitle       = new_pagetitle
                longtitle       = new_longtitle
                description     = row['title_game'] + " 1win online game &#127875; for free play 1win with Pragmatic play. Spin the reels " + row['title_game'] +" and take Bonus in this game"
                alias           = row['alias']
                menuindex       = 0
                template        = 29
                res_context_key = "web"
                b0_res_content  = text_game_NLTK
                b0_image        = "games/" + row['image_0']
                createdon       = int(time.time())
                published       = 1
                hidemenu        = 0
                sort_num        = 2
                b1_content_h2   = ''
                b1_content_json = b1_content_json
                b1_demo_iframe  = ''
                b1_comments_h2  = ''
                b1_comments_image = ''
                b1_comments_json = ''
                image_galer_h2  = 'Images ' + row['title_game']
                image_galer_json = image_galer_json
                faq_block_h2    = ''
                faq_block_json  = ''
                keywords        = 0
                new_block_p_json = ''
                editedon        = 0
                editedby        = 0
                createdby       = 0
                deleted         = 0
                deletedon       = 0
                deletedby       = 0
                publishedon     = 0
                unpublishedon   = 0
                publishedby     = 0
                b1_youtubeorvideo_h2 = ''
                b1_youtube_rolik = ''
                b1_video_rolik  = f"games/{row['alias']}/images/{row['alias']}.mp4"
                b1_anime_image  = ''
                img_mini = img_mini

                # Составляем SQL запрос для вставки данных
                sql_query = """
                INSERT INTO modx_gameall_co
                (resource_id, pagetitle, longtitle, description, alias, menuindex, template, res_context_key, b0_res_content, b0_image, img_mini, createdon, published, hidemenu, sort_num, b1_content_h2, b1_content_json, b1_demo_iframe, b1_comments_h2, b1_comments_image, b1_comments_json, image_galer_h2, image_galer_json, faq_block_h2, faq_block_json, keywords, new_block_p_json, editedon, editedby, createdby, deleted, deletedon, deletedby, publishedon, unpublishedon, publishedby, b1_youtubeorvideo_h2, b1_youtube_rolik, b1_video_rolik, b1_anime_image)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                pagetitle = VALUES(pagetitle),
                longtitle = VALUES(longtitle),
                description = VALUES(description),
                menuindex = VALUES(menuindex),
                template = VALUES(template),
                res_context_key = VALUES(res_context_key),
                b0_res_content = VALUES(b0_res_content),
                b0_image = VALUES(b0_image),
                img_mini = VALUES(img_mini),
                createdon = VALUES(createdon),
                published = VALUES(published),
                hidemenu = VALUES(hidemenu),
                sort_num = VALUES(sort_num),
                b1_content_h2 = VALUES(b1_content_h2),
                b1_content_json = VALUES(b1_content_json),
                b1_demo_iframe = VALUES(b1_demo_iframe),
                b1_comments_h2 = VALUES(b1_comments_h2),
                b1_comments_image = VALUES(b1_comments_image),
                b1_comments_json = VALUES(b1_comments_json),
                image_galer_h2 = VALUES(image_galer_h2),
                image_galer_json = VALUES(image_galer_json),
                faq_block_h2 = VALUES(faq_block_h2),
                faq_block_json = VALUES(faq_block_json),
                keywords = VALUES(keywords),
                new_block_p_json = VALUES(new_block_p_json),
                editedon = VALUES(editedon),
                editedby = VALUES(editedby),
                createdby = VALUES(createdby),
                deleted = VALUES(deleted),
                deletedon = VALUES(deletedon),
                deletedby = VALUES(deletedby),
                publishedon = VALUES(publishedon),
                unpublishedon = VALUES(unpublishedon),
                publishedby = VALUES(publishedby),
                b1_youtubeorvideo_h2 = VALUES(b1_youtubeorvideo_h2),
                b1_youtube_rolik = VALUES(b1_youtube_rolik),
                b1_video_rolik = VALUES(b1_video_rolik),
                b1_anime_image = VALUES(b1_anime_image)
                """
                val = (resource_id, pagetitle, longtitle, description, alias, menuindex, template, res_context_key, b0_res_content, b0_image, img_mini, createdon, published, hidemenu, sort_num, b1_content_h2, b1_content_json, b1_demo_iframe, b1_comments_h2, b1_comments_image, b1_comments_json, image_galer_h2, image_galer_json, faq_block_h2, faq_block_json, keywords, new_block_p_json, editedon, editedby, createdby, deleted, deletedon, deletedby, publishedon, unpublishedon, publishedby, b1_youtubeorvideo_h2, b1_youtube_rolik, b1_video_rolik, b1_anime_image)


                # Выполнение запроса
                cursor.execute(sql_query, val)
                connect_database.commit()

except Exception as ex:
    print("Произошла ошибка при подключении к базе данных.")
    print(ex)
finally:
    if connect_database:
        connect_database.close()
        print("Соединение с базой данных закрыто.")
