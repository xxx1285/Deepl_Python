class Profile:
    def __init__(self, name, user_agent, country, proxy=None, start_url="https://www.booking.com/"):
        self.name = name
        self.user_agent = user_agent
        self.country = country
        self.proxy = proxy
        self.start_url = start_url

    def __str__(self):
        return f"Profile(name={self.name}, user_agent={self.user_agent}, proxy={self.proxy})"

    def to_dict(self):
        """
        Преобразует профиль в словарь для сериализации.
        """
        return {
            "name": self.name,
            "user_agent": self.user_agent,
            "country": self.country,
            "proxy": self.proxy,
            "start_url": self.start_url
        }

    @classmethod
    def from_dict(cls, data):
        """
        Создает экземпляр Profile из словаря.

        :param data: Словарь с данными профиля.
        :return: Экземпляр Profile.
        """
        return cls(data["name"], data["user_agent"], data.get("country"), data.get("proxy"), data["start_url"])
