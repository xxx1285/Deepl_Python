import time
import re
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException, \
                                        ElementClickInterceptedException, InvalidArgumentException

# Captcha IMG
from app_captcha.captcha_Tesseract_img import captcha_tesseract_image
# EMAIL
from app.app_email_genera_and_openLink  import  generate_email, check_mailbox
# Auto Text Generate
from app.app_generate_text import generate_text_about_us

def solve_math_problem(text):
    try:
        # Используем регулярные выражения для поиска чисел и операторов в тексте
        match = re.match(r'(\d+)\s*([-+*/])\s*(\d+)\s*=', text)
        if match:
            # Извлекаем числа и оператор из совпавших групп
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            
            # Вычисляем результат в зависимости от оператора
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                result = num1 / num2  # Деление, здесь результат будет float
            else:
                raise ValueError("Неподдерживаемый оператор")
            
            return result
        else:
            raise ValueError("Неправильный формат текстовой задачи")
    except Exception as e:
        print(f"Ошибка при разборе текста: {e}")
        return None
    

def process_data(driver, post_url, my_site_url, unique_login, password, save_result):
    max_attempts = 3  # Максимальное количество попыток
    attempts = 0
    
    while attempts < max_attempts:

        try:
            driver.get(post_url)
            time.sleep(5)

            login = driver.find_element(By.XPATH, '//*[@id="createaccount-form0"]/div[1]/div/input')
            login.send_keys(unique_login)
            email = driver.find_element(By.XPATH, '//*[@id="ca-email"]')
            new_email = generate_email()
            email.send_keys(new_email)
            passwords = driver.find_element(By.XPATH, '//*[@id="createaccount-form0"]/div[4]/div/input')
            passwords.send_keys(password)
            repasswords = driver.find_element(By.XPATH, '//*[@id="createaccount-form0"]/div[5]/div/input')
            repasswords.send_keys(password)
            captcha = captcha_tesseract_image(driver, '//*[@id="createaccount-captcha"]/div/span[1]/img')
            print(captcha)
            res_math_captcha = solve_math_problem(captcha)
            input_res_math_captcha = driver.find_element(By.XPATH, '//*[@id="createaccount-captcha"]/div/input[1]')
            input_res_math_captcha.send_keys(res_math_captcha)
            print(res_math_captcha)
            driver.find_element(By.XPATH, '//*[@id="createaccount-form0"]/div[8]/input').click()
            time.sleep(5)
            verifid_link = check_mailbox(new_email)
            driver.get(verifid_link)
            print(verifid_link)
            time.sleep(3)

            # profile_knopka = driver.find_element(By.XPATH, '//*[@id="skrollr-body"]/div[1]/nav/div[1]/div[1]/div[3]/div/div')
            # ActionChains(driver).move_to_element(profile_knopka).click().perform()

            #   відкриваємо розділ де ставити лінку
            driver.get('https://www.wikidot.com/account/settings#/about')
            time.sleep(3)
            #   ставим LINK
            driver.find_element(By.NAME, 'website').send_keys(my_site_url)

            # ставим ТЕКСТ в ABOUT
            generate_text = generate_text_about_us(my_site_url)
            driver.find_element(By.NAME, 'about').send_keys(generate_text)
            print(generate_text)

            #   зберігаємо внесений сайт та настройки
            driver.find_element(By.XPATH, '//*[@id="dp-about-form"]/div[10]/div/a').click()

            # driver.get("https://whoer.net/ru")
            time.sleep(3)

            ########################################################################
            # ОТРИМУЄМО ТА ЗБЕРІГАЄМО ЛІНКА
            ########################################################################
            driver.get('https://www.wikidot.com/account/settings#/forumsignature')
            # Поиск ссылки по XPath
            link_element = driver.find_element(By.XPATH, "//a[contains(@href, 'wikidot.com/user:info')]")
            # Получение значения атрибута href у найденной ссылки
            link_href = link_element.get_attribute("href")
            with open(save_result, 'a') as file:
                # Записываем link_href в файл с новой строки
                file.write(link_href + '\n')
            print("Полный адрес найденной ссылки:", link_href)
            
            break  # Если всё прошло успешно, выходим из цикла
            
        except TimeoutException:
            print("Страница не загрузилась за 30 секунд")

        except Exception as e:
            attempts += 1
            print(f"Ошибка при выполнении функции process_data: {e}")
            if attempts == max_attempts:
                print(f"Достигнуто максимальное количество попыток ({max_attempts}). Прекращаем выполнение функции.")



        #     {"r_reg_nazva_bloga_find": """reg_nazva = driver.find_element(By.XPATH, '/html/body/div[7]/c-wiz/div/c-wiz/div[1]/span/div[2]/div/div/div[1]/div/div[1]/input')"""},
    #     {"r_reg_nazva_bloga_input": """reg_nazva.send_keys("The dog house game my blog")"""},