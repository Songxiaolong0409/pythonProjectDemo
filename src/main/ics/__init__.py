from src.main.environment import Environment


class ICS(Environment):

    def dev(self):
        pass

    def test(self):
        return self.__init__(
            url="http://121.40.88.181:48279",
            client_id="console_911427",
            client_secret="Fih793987",
            grant_type="password",
            usertype="8540868",
            username="admin",
            password="Fih123456"
        )

    def pre(self):
        return self.__init__(
            url="http://47.56.210.117:48279",
            client_id="console_911427",
            client_secret="Fih793987",
            grant_type="password",
            usertype="8540868",
            username="admin",
            password="Fih123456"
        )

    def prd(self):
        pass

    def aws(self):
        pass
