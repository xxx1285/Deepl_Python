from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from app.profile import Profile

class BrowserLauncher:
    def __init__(self):
        # Настройки для WebDriver, если требуется
        self.driver_options = webdriver.ChromeOptions()

    def launch_browser(self, profile):

        # Запуск WebDriver для антидетект браузера
        self.chrome_options = Options()

        self.chrome_options.add_argument("--disable-notifications")
        if profile.user_agent:
            self.chrome_options.add_argument(f"user-agent={profile.user_agent}")
        # убираем надпись о Тестовом ПО в Браузере
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.chrome_options.add_experimental_option('useAutomationExtension', False)

        self.ser = Service(executable_path=r"D:\Gembling\Deepl_Python\Deepl_Python\SETTINGS\Chrome\109.0.5414.25\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser, options=self.chrome_options)
        self.driver.get(profile.start_url or "https://www.bbc.com/news")
        self.driver.maximize_window()

    def close_browser(self):
        """
        Закрывает браузер.
        """
        if self.driver:
            self.driver.quit()
