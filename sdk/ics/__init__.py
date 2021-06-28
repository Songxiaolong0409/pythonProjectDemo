from enum import Enum

from sdk.profilesActive import ProfilesActiveEnum

AREA_CODE = "+86"


class IcsEnum(Enum):
    URL = "url"
    CLIENT_ID = "client_id"
    CLIENT_SECRET = "client_secret"
    USERTYPE = "usertype"


class Environment(object):
    __attr__ = [
        IcsEnum.URL,
        IcsEnum.CLIENT_ID,
        IcsEnum.CLIENT_SECRET,
        IcsEnum.USERTYPE]

    def __init__(self, url, client_id, client_secret, usertype):
        self.url = url
        self.client_id = client_id
        self.client_secret = client_secret
        self.usertype = usertype

    @staticmethod
    def __test():
        return Environment(
            "http://121.40.88.181:48279",
            "console_911427",
            "Fih793987",
            "8540868")

    @staticmethod
    def __pre():
        # return Environment(
        #     "http://47.56.210.117:48279",
        #     "console_911427",
        #     "Fih793987",
        #     "8540868")
        return Environment(
            "http://47.56.210.117:48279",
            "PSSPatient_084412",
            "Fih987113",
            "29893215")

    @staticmethod
    def get_ics_environment(environment):
        if environment == ProfilesActiveEnum.TEST.value:
            return Environment.__test()
        elif environment == ProfilesActiveEnum.PRE.value:
            return Environment.__pre()
        else:
            return Environment.__test()
