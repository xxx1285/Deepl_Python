websites = {
    # "https://www.blogger.com/": [
    #     {"r_knopkа_Sozdat_Blog_and_click": """my_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="maincontent"]/section[1]/header/a'))).click()"""},
    #     {"r_google_autorization": """my_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')))"""},
    #     {"r_google_authorization_function": "gmail_autoriz_fun(driver, email, password)"},
    #     {"r_reg_ozidaem_zagruzku_site": """my_wait.until(EC.url_contains("blogger.com"))"""},
    #     {"r_reg_nazva_bloga_find": """reg_nazva = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input')"""},
    #     {"r_reg_nazva_bloga_input": """reg_nazva.send_keys("The dog house game my blog")"""},
    #     {"r_reg_nazva_bloga_click_next": """driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[3]/div[2]/div/div[2]/div[2]/span/span').click()"""},
    #     {"r_reg_url_bloga_wait": "time.sleep(1)"},
    #     {"r_reg_url_bloga_find_input": """reg_url = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input')"""},
    #     {"r_reg_url_bloga_input": """reg_url.send_keys("the-dog-house23")"""},
    #     {"r_reg_url_bloga_click_next": """driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[3]/div[2]/div/div[2]/div[2]/span/span').click()"""},
    #     {"r_author_name_wait": "time.sleep(1)"},
    #     {"r_author_name_input": """author_name = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input')"""},
    #     {"r_author_name_click_next": """author_name.send_keys("Alexandr Riddic")"""},
    #     {"new_post_wait_and_click": """my_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div[4]/div[2]/div/c-wiz/div[2]/div/div/span/span/span[2]'))).click()"""},
    #     {"post_write_title": """post_nazva = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[2]/div/c-wiz/div/div[1]/div[1]/div[1]/div/div[1]/input')"""},
    #     {"post_write_title": """post_nazva.send_keys("My Post About - The dog house game my blog 2")"""},
    #     {"knopka_in_HTML_code": """html_knopka = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]')"""},
    #     {"knopka_in_HTML_code_action": "ActionChains(driver).move_to_element(html_knopka).click().perform()"},
    #     {"knopka_in_HTML_code_2": """html_knopka2 = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]')"""},
    #     {"knopka_in_HTML_code_action_2": "ActionChains(driver).move_to_element(html_knopka2).click().perform()"},
    #     {"post_write_text_find_block": """post_text = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz[2]/div/c-wiz/div/div[2]/div/div/div[3]/span/div/div[2]/div[2]/div/div/div/div[6]')"""},
    #     {"post_write_text_click_block": "ActionChains(driver).move_to_element(post_text).click().perform()"},
    #     {"post_write_text": """post_text.send_keys("My_Tedxt*******************")"""},
    #     {"link_post_click": """driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/div/span/div/div').click()"""},
    #     {"link_post_text": """link_post_text = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div/div[2]/div/div/div[4]/span/c-wiz/div/div[2]/div[3]/span/div[1]/span').text"""},
    #     {"print_link": "print(link_post_text)"},
    #     {"click_publish_1": """driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div/div[1]/div[2]/div[4]/span').click()"""},
    #     {"click_publish_2": """my_wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[4]/div/div[2]/div[3]/div[2]'))).click()"""},
    #     {"time_wait_2": "time.sleep(2)"},
    # ],
    "https://blogs.cornell.edu/advancedrevenuemanagement12/2012/03/28/revenue-management-in-the-golf-industry/comment-page-77/": [
        {"wait_load_click": """my_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="comment"]'))).click()"""},
        {"comment_find": """comment = driver.find_element(By.XPATH, '//*[@id="comment"]')"""},
        {"comment_input": """comment.send_keys(my_new_comment)"""},
        {"captcha": """text_captcha = process_image(driver, 'secureimg')"""},
        {"captcha_find_": """captcha_find = driver.find_element(By.XPATH, '//*[@id="securitycode"]')"""},
        {"captcha_and_click": """ActionChains(driver).move_to_element(captcha_find).click().perform()"""},
        {"captcha_input_text": """captcha_find.send_keys(text_captcha)"""},
        {"author_find_and_input_text": """driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(email_json_info['author'])"""},
        {"email_find_and_input_text": """driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email_json_info['login'])"""},
        {"checkbox_find_and_click": """driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()"""},
        {"button_find_and_click": """driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""},
    ]
}

# https://www.blogger.com/onboarding?pli=1#create


# pass_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
#         password_input = my_wait.until(EC.presence_of_element_located((By.XPATH, pass_xpath)))


# //*[@id="yDmH0d"]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input
# //*[@id="yDmH0d"]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input
        # password_input = my_wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div/div[1]/div/div[2]/div[2]')))
        
        # # Введення пароля
        # password_input.send_keys(password)
        # # Знаходимо кнопку - далі
        # next_button_pass = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span')
        # ActionChains(driver).move_to_element(next_button_pass).click(next_button_pass).perform()