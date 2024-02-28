import random

def get_device_emulation_settings():
    device_type = random.choice(['mobile'])

    if device_type == 'mobile':
        devices = {
            'iPhone SE': {
                "deviceName": "iPhone SE"
            },
            'iPhone XR': {
                "deviceName": "iPhone XR"
            },
            'iPhone X': {
                "deviceName": "iPhone X"
            },
            'iPhone XR': {
                "deviceName": "iPhone XR"
            },
            'Samsung Galaxy S8+': {
                "deviceName": "Samsung Galaxy S8+"
            },
            'Samsung Galaxy S8+': {
                "deviceName": "Samsung Galaxy S8+"
            },
            'Pixel 7': {
                "deviceName": "Pixel 7"
            },
            'Pixel 7': {
                "deviceName": "Pixel 7"
            },
            'iPhone 12 Pro': {
                "deviceName": "iPhone 12 Pro"
            },
            'iPad Air': {
                "deviceName": "iPad Air"
            },
            'Surface Pro 7': {
                "deviceName": "Surface Pro 7"
            }
        }
        chosen_device = random.choice(list(devices.keys()))
        return devices[chosen_device]

    else:
        desktop_settings = [
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            },
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            },
            {
                "userAgent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
            },
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            },
            {
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
            }
            # Другие настройки user-agent для разных десктопных устройств можно добавить здесь
        ]
        chosen_setting = random.choice(desktop_settings)
        return chosen_setting
