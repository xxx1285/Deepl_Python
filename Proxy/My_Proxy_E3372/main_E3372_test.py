from test_E3372 import toggle_mobile_data_switch_and_wait_for_ip

# Пример использования
host_ip = '192.168.8.1'
enable_data = True  # Установите в False для выключения мобильных данных

toggle_mobile_data_switch_and_wait_for_ip(host_ip, enable_data)
