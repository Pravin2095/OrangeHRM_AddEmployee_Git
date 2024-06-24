import configparser

Configuration = configparser.RawConfigParser()

Configuration.read("G:\\Python\\OrangeHRM\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def geturl():
        url = Configuration.get('common info','url')
        return url

    @staticmethod
    def getusername():
        Username = Configuration.get('common info', 'Username')
        return Username

    @staticmethod
    def getpassword():
        Password = Configuration.get('common info', 'Password')
        return Password