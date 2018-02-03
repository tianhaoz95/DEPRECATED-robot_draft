from .util import get_impl

class Robot:
    __instance = None

    def __init__(self, mode=None, info=None):
        """ Create robot instance """
        if Robot.__instance is None:
            robot_impl = get_impl(mode, info)
            Robot.__instance = robot_impl()
        self.__dict__['_Robot__instance'] = Robot.__instance

    def __getattr__(self, attr):
        """ Delegate access to actual robot implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to actual robot implementation """
        return setattr(self.__instance, attr, value)
