import random

def get_firefox_emulation_settings():
    device_type = random.choice(['mobile', 'desktop'])

    if device_type == 'mobile':
        mobile_settings = [
            # # iPhone X
            # {
            #     "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            #     "windowSize": "375,812"
            # },
            # # iPad
            # {
            #     "userAgent": "Mozilla/5.0 (iPad; CPU OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            #     "windowSize": "768,1024"
            # },
            # # Google Pixel 3 XL
            # {
            #     "userAgent": "Mozilla/5.0 (Linux; Android 9; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
            #     "windowSize": "412,847"
            # },
            # # Samsung Galaxy S8
            # {
            #     "userAgent": "Mozilla/5.0 (Linux; Android 8.0; Samsung Galaxy S8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36",
            #     "windowSize": "360,740"
            # },
            # Surface Pro 7
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0",
                "windowSize": "1280,720"
            },
            # # iPad Air
            # {
            #     "userAgent": "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148",
            #     "windowSize": "820,1180"
            # },
            # Другие мобильные настройки...
        ]
        chosen_setting = random.choice(mobile_settings)
        return chosen_setting

    else:
        desktop_settings = [
            # Обычный Windows 10 десктоп
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
                "windowSize": "1920,1080"
            },
            # MacBook Air
            {
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
                "windowSize": "1440,900"
            },
            # Linux десктоп
            {
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
                "windowSize": "1366,768"
            },
            # Windows 7 десктоп
            {
                "userAgent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "windowSize": "1600,900"
            },
            # iMac
            {
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15",
                "windowSize": "2560,1440"
            },
            # Обычный Windows 10 десктоп (второй вариант)
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
                "windowSize": "1920,1080"
            },
            # Windows 7 десктоп (второй вариант)
            {
                "userAgent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "windowSize": "1366,768"
            },
            # Internet Explorer 11 на Windows 10
            # {
            #     "userAgent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
            #     "windowSize": "1600,900"
            # },
            # Firefox на Windows 10
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0",
                "windowSize": "1440,900"
            },
            # Высокое разрешение Windows 10
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
                "windowSize": "2560,1440"
            },
            # Другие десктопные настройки...
        ]
        chosen_setting = random.choice(desktop_settings)
        return chosen_setting
