websites = {
    "https://blogs.cornell.edu/advancedrevenuemanagement12/2012/03/28/revenue-management-in-nail-salon-industry-selling-your-time-and-space/": [
        {"a2": """a2 = driver.find_element(By.XPATH, '//*[@id="comment"]').send_keys(my_spam_comment)"""},
        {"a6": """a6 = driver.find_element(By.XPATH, '//*[@id="author"]').send_keys(my_spam_author)"""},
        {"a8": """a8 = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(my_spam_email)"""},
        {"a9": """a9 = driver.find_element(By.XPATH, '//*[@id="wp-comment-cookies-consent"]').click()"""},
        {"captcha_1": """captcha_img_XPATH = '//*[@id="secureimg"]'"""},                                            # XPATH images
        {"captcha_2": """captcha_img_XPATH_text = fun_my_captcha_image(driver, captcha_img_XPATH)"""},
        {"captcha_3": """captcha_find_input_text = driver.find_element(By.XPATH, '//*[@id="securitycode"]')"""},    # XPATH поле ввода
        {"captcha_4": """ActionChains(driver).move_to_element(captcha_find_input_text).click().perform()"""},
        {"captcha_5": """captcha_find_input_text.send_keys(captcha_img_XPATH_text)"""},
        {"a10": """a10 = driver.find_element(By.XPATH, '//*[@id="submit"]').click()"""},
        ],
    
}