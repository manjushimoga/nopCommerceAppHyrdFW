import configparser

config = configparser.RawConfigParser()

config.read("./Configurations/config.ini")

class ReadConfig():
    @staticmethod
    def get_application_URL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info','username')
        return username

    @staticmethod
    def get_password():
        pwd = config.get('common info','password')
        return pwd
