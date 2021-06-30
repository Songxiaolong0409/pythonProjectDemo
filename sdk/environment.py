from abc import ABCMeta, abstractmethod

from sdk.profilesActive import ProfilesActiveEnum


class Environment(object):

    __metaclass__ = ABCMeta  # 这是一个抽象类

    @abstractmethod
    def dev(self):
        pass

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def pre(self):
        pass

    @abstractmethod
    def prd(self):
        pass

    @abstractmethod
    def aws(self):
        pass

    @staticmethod
    def get_environment(environment, impl_obj):
        if environment == ProfilesActiveEnum.DEV.value:
            return impl_obj.dev()
        elif environment == ProfilesActiveEnum.TEST.value:
            return impl_obj.test()
        elif environment == ProfilesActiveEnum.PRE.value:
            return impl_obj.pre()
        elif environment == ProfilesActiveEnum.PRD.value:
            return impl_obj.prd()
        elif environment == ProfilesActiveEnum.AWS.value:
            return impl_obj.aws()
        else:
            return impl_obj.test()
