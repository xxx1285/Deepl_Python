import csv
import pymysql
import json
import os
import time


# SQL Config path
sql_config = r'VideoRec_from_SiteMonitor\3_Zaliv_PragmatGames_on_SQLsite\configs\config_sql.json'
with open(sql_config, 'r') as f:
    configSQL = json.load(f)
# Открываем CSV файл
csv_file_path = r'VideoRec_from_SiteMonitor\output_PragmaticGames\output_games.csv'


try:
    # Подключаемся к базе данных
    connect_database = pymysql.connect(**configSQL['config_database'],
                                       port=3306,
                                       cursorclass=pymysql.cursors.DictCursor)
    with connect_database.cursor() as cursor:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Создаем JSON массив для image_galer_json
                image_galer_json_list = []
                for i in range(1, 6):
                    image_galer_json_list.append({
                        "MIGX_id": str(i),
                        "description": f"image slot {row['title_game']} - {i} play",
                        "image": f"games/{row['alias']}/scrin-images/image-slot-{row['alias']}-{i}"
                    })
                image_galer_json = json.dumps(image_galer_json_list)

                # SQL tables
                resource_id     = 484
                pagetitle       = row['title_game']
                longtitle       = "1win " + row['title_game'] + " slot demo Pragmatic play - 1win casino"
                createdon       = int(time.time())
                description     = row['title_game'] + " demo slot game &#127875; for free play with our play version Pragmatic play. No deposit required! Spin the reels " + row['title_game'] +" and experience this epic game"
                alias           = row['alias']
                menuindex       = 0
                template        = 29
                res_context_key = "web"
                b0_res_content  = row['text_game']
                b0_image        = "games/" + row['alias'] + "/scrin-images/image-slot-" + row['alias'] + "-0"
                createdon       = int(time.time())
                published       = 1
                hidemenu        = 0
                sort_num        = 2
                b1_content_h2   = ''
                b1_content_json = ''
                b1_demo_iframe  = row['iframe_url']
                b1_comments_h2  = ''
                b1_comments_image = ''
                b1_comments_json = ''
                image_galer_h2  = 'Demo images slot ' + row['title_game']
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
                b1_youtubeorvideo_h2 = "Video slot " + row['title_game']
                b1_youtube_rolik = ''
                b1_video_rolik  = "games/" + row['alias'] + "/video/video-" + row['alias'] + ".mp4"

                # Составляем SQL запрос для вставки данных
                sql_query = """
                INSERT INTO modx_gameall_co
                (resource_id, pagetitle, longtitle, description, alias, menuindex, template, res_context_key, b0_res_content, b0_image, createdon, published, hidemenu, sort_num, b1_content_h2, b1_content_json, b1_demo_iframe, b1_comments_h2, b1_comments_image, b1_comments_json, image_galer_h2, image_galer_json, faq_block_h2, faq_block_json, keywords, new_block_p_json, editedon, editedby, createdby, deleted, deletedon, deletedby, publishedon, unpublishedon, publishedby, b1_youtubeorvideo_h2, b1_youtube_rolik, b1_video_rolik)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                pagetitle = VALUES(pagetitle),
                longtitle = VALUES(longtitle),
                description = VALUES(description),
                menuindex = VALUES(menuindex),
                template = VALUES(template),
                res_context_key = VALUES(res_context_key),
                b0_res_content = VALUES(b0_res_content),
                b0_image = VALUES(b0_image),
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
                b1_video_rolik = VALUES(b1_video_rolik)
                """
                val = (resource_id, pagetitle, longtitle, description, alias, menuindex, template, res_context_key, b0_res_content, b0_image, createdon, published, hidemenu, sort_num, b1_content_h2, b1_content_json, b1_demo_iframe, b1_comments_h2, b1_comments_image, b1_comments_json, image_galer_h2, image_galer_json, faq_block_h2, faq_block_json, keywords, new_block_p_json, editedon, editedby, createdby, deleted, deletedon, deletedby, publishedon, unpublishedon, publishedby, b1_youtubeorvideo_h2, b1_youtube_rolik, b1_video_rolik)


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
